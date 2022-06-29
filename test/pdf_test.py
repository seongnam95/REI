from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer


# 등기부등본 List 변경
def get_register(path):
    datas = []
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser)

    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        layout = device.get_result()

        datas.append(parse_obj(layout._objs))
    return sum(datas, [])


def parse_obj(lt_objs):
    data = []
    for obj in lt_objs:
        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            # d = "%6d, %6d, %s" % (obj.bbox[0], obj.bbox[1], obj.get_text().replace('\n', ''))
            # static.append(d)
            data.append(obj.get_text().replace('\n', '_'))
        elif isinstance(obj, pdfminer.layout.LTFigure): parse_obj(obj._objs)
    return data


def extract(page):
    title_index, datas, result = [], [], {}
    for i, c in enumerate(page):
        if '【' in c:
            title_index.append(i)
        elif '이하여백' in c.replace(" ", ""):
            title_index.append(i)

    title_index.append(len(page))
    start_index = 0

    # 제목별로 리스트 추가
    for n, t in enumerate(title_index):
        datas.append(page[start_index:t])
        start_index = t
    print(datas)
    # 제목별로 딕셔너리 정리
    for data in datas:
        if '표제부' in data[0].replace(" ", ""):
            result['표제부'] = data
        elif '갑구' in data[0].replace(" ", ""):
            result['갑구'] = data
        elif '을구' in data[0].replace(" ", ""):
            result['을구'] = data

    result['타입'] = datas[0][1].split('- ')[1].split(' -')[0]
    result['소재지'] = datas[0][3].split('] ')[1].split('_')[0]

    return result


file_name = 'test_pdf2.pdf'
val = get_register(file_name)

owner, owners = {}, []
r_data = extract(val)
for i in r_data['갑구']:
    print(i)
    if '*' in i:
        for n in i.split('_'):
            print(n)
            if '집합' in r_data['타입']:
                if '분의' in n:
                    owner['지분'] = n.split('지분 ')[1]
                elif '*' in n:
                    owner['이름'] = n.split('  ')[0]
                    owner['생년월일'] = n.split('  ')[1].split('-')[0]
            else:
                if '*' in n:
                    name = n.split('소유자  ')[1]
                    owner['이름'] = name.split('  ')[0]
                    owner['생년월일'] = name.split('  ')[1].split('-')[0]

        owners.append(owner)
        owner = {}
        print(owners)

for i in owners:
    if '지분' in i.keys():
        print('소유자명 %s, 생년월일 %s, 지분 %s' % (i['이름'], i['생년월일'], i['지분']))
    else:
        print('소유자명 %s, 생년월일 %s' % (i['이름'], i['생년월일']))


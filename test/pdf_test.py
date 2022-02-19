from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer


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
            # data.append(d)
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
    for n, t in enumerate(title_index):
        datas.append(page[start_index:t])
        start_index = t

    for data in datas:
        if '갑구' in data[0].replace(" ", ""):
            result['갑구'] = data
        elif '을구' in data[0].replace(" ", ""):
            result['을구'] = data

    return result


file_name = 'test_pdf3.pdf'
val = get_register(file_name)

owner, owners = {}, []
for i in extract(val)['갑구']:
    if '*' in i:
        for n in i.split('_'):
            print(i)
            if '분의' in n:
                owner['지분'] = n.split('지분 ')[1]
            elif '*' in n:
                owner['이름'] = n.split('  ')[0]
                owner['생년월일'] = n.split('  ')[1].split('-')[0]
        owners.append(owner)
        owner = {}

for i in owners:
    if '지분' in i.keys():
        print('소유자명 %s, 생년월일 %s, 지분 %s' % (i['이름'], i['생년월일'], i['지분']))
    else:
        print('소유자명 %s, 생년월일 %s' % (i['이름'], i['생년월일']))


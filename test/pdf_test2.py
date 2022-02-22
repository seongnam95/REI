import camelot
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)
pd.set_option('display.width', None)


def table_trim(path):
    tables = camelot.read_pdf(path, pages="all", kind= "line")
    keys, result = [], []
    print(tables)
    # # 테이블 수 만큼 반복
    # for table in tables:
    #     title_idx = []
    #     frame = table.df
    #     print(frame)
    # return result


def extract(frame):
    result = {}
    for f in frame:
        if f.iloc[0][0] == '표제부':
            val = f.iloc[2][2].replace('\n', ' ')
            if '[도로명주소]' in val:
                result['소재지'] = val.split(' [도로명주소] ')[0]
                result['도로명주소'] = val.split(' [도로명주소] ')[1]

            if f.iloc[1][2] == '건 물 번 호':
                result['소재지'] = "%s %s" % (result['소재지'], f.iloc[2][2])
                result['도로명주소'] = "%s %s" % (result['도로명주소'], f.iloc[2][2])

            if f.iloc[1][4] == '권리자 및 기타사항':
                owners = f.iloc[2][4]
                if '지분' in owners:
                    owners = owners.split('\n')
                    extract_owners, name, share = [], '', ''

                    for o in owners:
                        if '지분' in o:
                            share = o.split('지분 ')[1]
                        elif '*' in o:
                            name = '%s/%s' % (o.split('  ')[0], o.split('  ')[1].split('-')[0])
                        if name and share:
                            extract_owners.append("%s/%s" % (name, share))
                            name, share = '', ''

                    result['소유자'] = extract_owners
                else:
                    result['소유자'] = owners.split('소유자  ')[1].split('-')[0].replace('  ', '/')

        if f.iloc[0][0] == '대지권의목적인토지의표시':
            for i, s in enumerate(f.iloc[1]):
                if s == '대지권종류': result['대지권종류'] = f.iloc[2][i]
                elif s == '대지권비율': result['대지권비율'] = f.iloc[2][i]

    print(result['소유자'])


file_name = 'bd_test.pdf'
table_trim(file_name)

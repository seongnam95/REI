import camelot
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)
pd.set_option('display.width', None)


def table_trim(path):
    tables = camelot.read_pdf(path, pages="all")
    keys, result = [], []
    aa = tables[0].df
    print(aa[5])

    # 테이블 수 만큼 반복
    for table in tables:
        title_idx = []
        frame = table.df
        key = frame.iloc[:, 0]

        # 제목, 제목의 인덱스 추출
        for i, k in enumerate(key):
            if '【' in k:
                k = "%s%i" % (k, keys.count(k)) if k in keys else k.split('【')[1].split('】')[0].replace(' ', '')
                keys.append(k)
                title_idx.append(i)
            elif '(' in k:
                k = k.split('(')[1].split(')')[0].replace(' ', '')
                keys.append(k)
                title_idx.append(i)

        # 제목 인덱스 기준으로 데이터프레임 나누기
        for n, i in enumerate(title_idx):

            # 한 테이블에 여러 값이 있을 시 나누기
            if len(title_idx) > 1:
                if i != title_idx[-1]:
                    nxt = title_idx[n+1]
                    data = frame.iloc[i:nxt]
                    data.iloc[0][0] = keys[n]
                    result.append(data)
                else:
                    data = frame.iloc[i:len(frame)]
                    data.iloc[0][0] = keys[n]
                    result.append(data)

            # 한 테이블에 한 값만 있을 시
            else:
                frame.iloc[0][0] = keys[n]
                result.append(frame)
    return result


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


file_name = 'ggg.pdf'
response = table_trim(file_name)
for i in response:
    a = i.replace('\n', ' ')
    print(a)
    print("#" * 100)


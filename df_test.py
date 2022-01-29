import pandas as pd
from datetime import datetime

exclusive = pd.DataFrame({'층번호': ['1.0', '3.0', '1.0', '2.0', '2.0', '2.0'],
                          '층번호명': ['1층', '1층', '각층', '2층', '2층', '각층'],
                          '전유공용구분': ['전유', '전유', '공용', '전유', '전유', '공용'],
                          '호명칭': ['101호', '101호', '101호', '201호', '201호', '201호'],
                          '전용면적': ['45.3', '12.3', '8.3', '12.3', '37.3', '8.3']})

exclusive2 = pd.DataFrame({'층번호': ['2.0', '2.0', '3.0', '10.0', '21.0', '2.0', '3.0', '1.0'],
                           '층번호명': ['2층', '2층', '3층', '10층', '21층', '2층', '3층', '1층'],
                           '호명칭': ['201호', '202호', '301호', '1001호', '2001호', '203호', '301호', '101호']})

exclusive3 = pd.DataFrame({'층번호': ['1.0', '1.0', '1.0', '1.0'],
                           '층번호명': ['1층', '각층', '2층', '각층'],
                           '전유공용구분': ['전유', '공용', '전유', '공용'],
                           '호명칭': ['1001호', '1002호', '101호', '102호'],
                           '전용면적': ['45.3', '8.3', '12.3', '8.3']})

exclusive4 = pd.DataFrame({'호명칭': ['1002호', '1001호', '102호', '101호', '10001호', '10002호']})

exclusive5 = pd.DataFrame({'호명칭': ['102동101호', '102동102호', '1101동1001호', '1101동1002호', '10001호', '10002호']})


# 호수 정렬
def sorted_rooms_len(data):
    existing = data.sort_values(by=['호명칭'], axis=0)
    try:
        # 호명칭의 길이를 len 키에 담기
        data['len'] = data['호명칭']
        for i in range(len(data)):
            data['len'].iloc[i] = len(data['len'].iloc[i])

        # 호명칭 길이 중복 제거 후 리스트에 담기
        name_len = list(set(data['len']))
        name_len.sort()

        # 명칭이 짧은 순서대로, 호수명대로 정렬
        rooms = []
        for i in name_len:
            value = data[data['len'] == i].sort_values(by=['호명칭'], axis=0)
            rooms.append(value)
        result = pd.concat(rooms, ignore_index=True)

        return result

    except (ValueError, IndexError, TypeError):
        return existing


def sorted_rooms_flr(data):
    existing = data.sort_values(by=['호명칭'], axis=0)

    try:
        data['층번호'] = data['층번호'].str.replace('.0', '')
        data['층번호명'] = data['층번호명'].str.extract('(\d+)')

        name = [x for x in list(set(data['층번호명'])) if pd.isnull(x) is False]
        num = list(set(data['층번호']))
        num.sort()
        print(data['층번호'])
        rooms = []
        if len(num) == len(name):
            for i in num:
                value = data[data['층번호'] == i].sort_values(by=['호명칭'], axis=0)
                rooms.append(value)
            result = pd.concat(rooms, ignore_index=True)
            return True, result

        else:
            return False, existing

    except (ValueError, IndexError, TypeError) as e:
        print(e)
        return False, existing


print(sorted_rooms_flr(exclusive2))


# 정확한 전유 호수 찾기
def get_exact_value(data):
    try:
        items = data

        # 전유 부분만
        items = items[items['전유공용구분'] == '전유']
        if len(items) == 0: return data

        # 층번호, 층번호명 비교 후 같은 층만 담기
        items = items[items['층번호'].str.rstrip('.0') == items['층번호명'].str.rstrip('층')]

        # 같은 층, 전유 항목이 2개 이상일 경우 면적 넓은 항목만 남기기
        hos = set(items['호수명'])
        if len(hos) == len(items): return items
        items = items.astype({'전용면적': 'float'})

        for i in hos:
            res = items[items['호수명'] == i]
            if len(res) == 1: continue
            items[items['호수명'] == i] = res.nlargest(1, '전용면적', keep='first')

        items = items.astype({'전용면적': 'str'}).dropna(axis=0)
        return items

    except ValueError:
        return data

import pandas as pd
# aa
exclusive = pd.DataFrame({'층번호': ['1.0', '3.0', '1.0', '2.0', '2.0', '2.0'],
                          '층번호명': ['1층', '1층', '각층', '2층', '2층', '각층'],
                          '전유공용구분': ['전유', '전유', '공용', '전유', '전유', '공용'],
                          '호수명': ['101호', '101호', '101호', '201호', '201호', '201호'],
                          '전용면적': ['45.3', '12.3', '8.3', '12.3', '37.3', '8.3']})

exclusive2 = pd.DataFrame({'층번호': ['1.0', '1.0', '1.0', '2.0', '2.0', '2.0'],
                           '층번호명': ['1층', '1층', '각층', '2층', '2층', '각층'],
                           '전유공용구분': ['전유', '전유', '공용', '전유', '전유', '공용'],
                           '호수명': ['101호', '101호', '101호', '201호', '201호', '201호'],
                           '전용면적': ['45.3', '12.3', '8.3', '12.3', '37.3', '8.3']})


exclusive3 = pd.DataFrame({'층번호': ['1.0', '1.0', '2.0', '2.0'],
                           '층번호명': ['1층', '각층', '2층', '각층'],
                           '전유공용구분': ['전유', '공용', '전유', '공용'],
                           '호수명': ['101호', '101호', '201호', '201호'],
                           '전용면적': ['45.3', '8.3', '12.3', '8.3']})

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

    except ValueError: return data


print(get_exact_value(exclusive))
print(get_exact_value(exclusive2))
print(get_exact_value(exclusive3))

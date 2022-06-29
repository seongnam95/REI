import pandas as pd

df1 = pd.DataFrame({'category': ['매매'],
                    'sort_num': ['1'],
                    'title': ['매매 기본 특약'],
                    'content': ['1. 가나다라마바사']})

df2 = pd.DataFrame({'category': ['매매', '매매'],
                    'sort_num': ['1', '2'],
                    'title': ['매매 기본 특약', '매매 기본 특약2'],
                    'content': ['1. 가나다라마바사', '2. 아자차카타파하']})

result = df2.combine_first(df1)

for idx in df2.index:
    row = df2.loc[idx]
    if row['category'] in df1['category'].values:
        if row['title'] in df1['title'].values:
            target_idx = df1[df1['title'] == row['title']].idex

            df1['sort_num'].loc[target_idx] = row['sort_num']
            df1['title'].loc[target_idx] = row['title']
            df1['content'].loc[target_idx] = row['content']

    else:
        df1 = pd.concat(df1, row)

print(df1)

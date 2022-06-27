import pymysql
import pandas as pd
import numpy as np


data = pd.read_csv('../test/busan.csv', sep="|")
data = data.replace(np.nan, 'NULL')
data = data.drop(columns=['우편일련번호', '시도영문', '시군구영문', '읍면영문', '도로명영문', '지하여부', '다량배달처명', '시군구용건물명', '산여부', '읍면동일련번호'])
data = data.astype(str)

columns = ', '.join(f"`{i}`" for i in data.columns)
values = ', '.join(f"%s" for _ in range(len(data.columns)))
sql = f'INSERT INTO `post_num_db` VALUES '

############################ PyMySQL
conn = pymysql.connect(
    host='db.snserver.site', user='jsn0509', password='ks05090818@', db='dbjsn0509', charset='utf8')
cur = conn.cursor()

print('시작')

for idx, slice_data in enumerate(np.array_split(data, 1000)):
    print('%s / 1000' % idx)

    val = []
    for i in range(len(slice_data)):
        val.append(tuple(slice_data.values[i]))
    val_str = str(val).lstrip('[').rstrip(']')

    cur.execute(sql + val_str)
    conn.commit()

conn.close()

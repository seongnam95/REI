import pymysql

conn = pymysql.connect(
    host='db.snserver.site', user='jsn0509', password='ks05090818@', db='dbjsn0509', charset='utf8')

cur = conn.cursor()
a = '매매'
cur.execute(f"INSERT INTO contract_condition VALUES(NULL, 'jsn0509', {a}, '매매 기본특약', '가나다라마바사')")
conn.commit()
conn.close()

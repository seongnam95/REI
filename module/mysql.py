import pymysql.cursors
import pandas as pd


def connection():
    con = pymysql.connect(host="db.snserver.site",
                          user="jsn0509", password="ks05090818@",
                          db="dbjsn0509", charset="utf8",
                          autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    return con


def get_agrs(user):
    con = connection()

    try:
        curs = con.cursor()
        curs.execute(f"SELECT * FROM `contract_condition` WHERE `userPk`=(%s)", user)

        data = pd.DataFrame(curs.fetchall())

        if data.empty:
            data = pd.DataFrame(columns=['pk', 'userPk', 'category', 'categoryNum', 'title', 'titleNum', 'content'])

        data = data.sort_values(['categoryNum'], ascending=True)
        data = data.reset_index(drop=True)
        print(data)

    finally:
        con.close()

    return data


def set_agrs(data):
    con = connection()

    try:
        curs = con.cursor()

        for idx in data.index:
            result = data.loc[idx].values.tolist() * 2
            # result = [v.replace("'", "''") if type(v) == str else v for v in row]

            sql = f"INSERT INTO `contract_condition` VALUES (%s, %s, %s, %s, %s, %s, %s) " \
                  f"ON DUPLICATE KEY UPDATE `pk`=%s, `userPk`=%s, `category`=%s, `categoryNum`=%s, `title`=%s, `titleNum`=%s, `content`=%s"

            curs.execute(sql, result)
            con.commit()

    finally:
        con.close()

    return data


def del_agrs(pk):
    con = connection()

    try:
        curs = con.cursor()

        if type(pk) == list:
            sql = "DELETE FROM `contract_condition` WHERE `userPk`=%s AND `category`=%s"
        else:
            sql = "DELETE FROM `contract_condition` WHERE `pk`=%s"

        curs.execute(sql, pk)
        con.commit()
    except Exception as e:
        print('err: ', e)

    finally:
        con.close()

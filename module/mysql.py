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
        curs.execute(f"SELECT * FROM `contract_condition` WHERE `user_id`=(%s)", user)

        data = pd.DataFrame(curs.fetchall())
        data = data.sort_values(['category_num'], ascending=True)
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
            row = data.loc[idx].values.tolist()
            result = list(dict.fromkeys(row)) * 2
            result = [v.replace("'", "''") if type(v) == str else v for v in result]

            sql = f"INSERT INTO `contract_condition` VALUES (%s, %s, %s, %s, %s) " \
                  f"ON DUPLICATE KEY UPDATE `pk`=%s, `user_id`=%s, `category`=%s, `category_num`=%s, `content`=%s"

            curs.execute(sql, result)
            con.commit()

    finally:
        con.close()

    return data


def del_agrs(data):
    con = connection()

    try:
        curs = con.cursor()

        sql = "DELETE FROM `contract_condition` WHERE `pk`=%s"

        curs.execute(sql, data.pk)
        con.commit()

    finally:
        con.close()

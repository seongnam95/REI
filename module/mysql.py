import pymysql
import pandas as pd


def connection():
    con = pymysql.connect(host="db.snserver.site",
                          user="jsn0509",
                          password="ks05090818@",
                          db="dbjsn0509",
                          charset="utf8")
    return con


def get_agrs(user):
    con = connection()

    try:
        curs = con.cursor()

        columns = '`category_num`, `category`, `content`'
        curs.execute(f"SELECT {columns} FROM `contract_condition` WHERE `user_id`='{user}'")

        data = pd.DataFrame(columns=['category_num', 'category', 'content'])
        for idx, row in enumerate(curs.fetchall()):
            data.loc[idx] = list(row)

        data = data.sort_values(['category_num'], ascending=True)
        data = data.reset_index(drop=True)

    finally:
        con.close()

    return data


def set_agrs(user, data):
    con = connection()

    try:
        curs = con.cursor()


    finally:
        con.close()

    return data

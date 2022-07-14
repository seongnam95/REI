import pymysql.cursors
import pandas as pd
import data.sys_data as data


def connection():
    con = pymysql.connect(host="db.snserver.site",
                          user="jsn0509", password="ks05090818@",
                          db="dbjsn0509", charset="utf8",
                          autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    return con


def get_api_key():
    con = connection()
    try:
        curs = con.cursor()
        curs.execute(f"SELECT * FROM `api_keys`")

        result = {}
        for i in curs.fetchall():
            result[i['apiNm']] = i['apiKey']

    finally:
        con.close()
    return result


def get_agrs(user):
    con = connection()

    try:
        curs = con.cursor()
        curs.execute(f"SELECT * FROM `contract_condition` WHERE `userPk`=(%s)", user)

        result = pd.DataFrame(curs.fetchall())

        if result.empty:
            result = pd.DataFrame(columns=['pk', 'userPk', 'category', 'categoryNum', 'title', 'titleNum', 'content'])

        result = result.sort_values(['categoryNum'], ascending=True)
        result = result.reset_index(drop=True)
        print(result)

    finally:
        con.close()

    return result


def set_agrs(result):
    con = connection()
    try:
        curs = con.cursor()
        for idx in result.index:
            result = result.loc[idx].values.tolist() * 2
            sql = f"INSERT INTO `contract_condition` VALUES (%s, %s, %s, %s, %s, %s, %s) " \
                  f"ON DUPLICATE KEY UPDATE `pk`=%s, `userPk`=%s, `category`=%s, `categoryNum`=%s, `title`=%s, `titleNum`=%s, `content`=%s"
            curs.execute(sql, result)
            con.commit()
    finally:
        con.close()

    return result


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

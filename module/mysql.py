import pymysql


class ReadMysqlData:
    def __init__(self):
        super(ReadMysqlData, self).__init__()

    @staticmethod
    def connection():
        con = pymysql.connect(host="localhost",
                              user="root",
                              password="",
                              db="rei",
                              charset="utf8")
        return con

    def read_system_value(self):
        con = self.connection()
        try:
            curs = con.cursor()
            sql = "SELECT * FROM data"
            curs.execute(sql)
            rows = curs.fetchone()
        finally:
            con.close()
        return rows

    def check_id(self, user_id):
        con = self.connection()
        try:
            curs = con.cursor()
            sql = "SELECT EXISTS(SELECT *FROM user WHERE userID = %(id)s)"
            curs.execute(sql, {"id": user_id})

            check = curs.fetchone()[0]
        finally:
            con.close()
        return check

    def check_phone(self, user_phone):
        con = self.connection()
        try:
            curs = con.cursor()
            sql = "SELECT EXISTS(SELECT *FROM user WHERE userPhone = %(phone)s)"
            curs.execute(sql, {"phone": user_phone})

            check = curs.fetchone()[0]
        finally:
            con.close()
        return check

    def login(self, user_id, user_pw):
        con = self.connection()
        try:
            curs = con.cursor()
            sql = "SELECT EXISTS(SELECT *FROM user WHERE userID = %(id)s and userPW = %(pw)s)"
            curs.execute(sql, {"id": user_id, "pw": user_pw})

            check = curs.fetchone()[0]
        finally:
            con.close()
        return check

    def register(self, data):
        con = self.connection()
        try:
            curs = con.cursor()
            sql = """INSERT INTO user (userID, userPW, userName, userPhone, userRank, 
                    companyName, companyAddress, companyBoss, companyCall, companyNumber)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            curs.execute(sql, data)
            con.commit()

        finally:
            con.close()

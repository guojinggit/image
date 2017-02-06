#coding=utf-8
import MySQLdb

class Mysql:

    db_map_conn = {}

    def __init__(self, config):
        self.mysqlIp = config.get("mysql", "ip")
        self.mysqlPort = config.getint("mysql", "port")
        self.mysqlUser = config.get("mysql", "user")
        self.mysqlPwd = config.get("mysql", "passwd")


    def connect(self, db):
        conn = MySQLdb.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=db)
        self.db_map_conn[db] = conn
        return conn

    def selectDb(self, db):
        if db in self.db_map_conn.keys():
            return self.db_map_conn[db].cursor()
        else:
            return self.connect(db).cursor()



# conn= MySQLdb.connect(
#         "120.26.164.219",
#         port=3306,
#         user='root',
#         passwd='root522409',
#         db ='test',
#         )
# cur = conn.cursor()
# print cur.execute("select * from test")
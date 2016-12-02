#coding=utf-8
import MySQLdb

class Mysql:

    db_map_conn = {}

    def init(self, host, port, user, passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd


    def connect(self, db):
        print self.host
        print self.port
        print self.user
        print self.passwd
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
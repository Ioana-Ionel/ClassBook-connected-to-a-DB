import MySQLdb

class DB:
    conn=None

    def connect(self):
        self.conn= MySQLdb.connect(host='127.0.0.1', user='root', passwd='ioana', db='ClassBook')

    def query(self,sql):
        try:
            cursor=self.conn.cursor()
            cursor.execute(sql)
        except (AttributeError,MySQLdb.OperationalError):
            self.connect()
            cursor=self.conn.cursor()
            cursor.execute(sql)
        return cursor


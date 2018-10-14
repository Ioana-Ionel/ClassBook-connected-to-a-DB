import MySQLdb

db=('127.0.0.1', 'root','ioana','ClassBook')

class DB:
    def __init__(self):
        self.conn= MySQLdb.connect(host=db[0], user=db[1], passwd=db[2], db=db[3])

    def query(self,sql):
        try:
            cursor=self.conn.cursor()
            cursor.execute(sql)
        except (AttributeError,MySQLdb.OperationalError):
            cursor=self.conn.cursor()
            cursor.execute(sql)
        return cursor

    def close(self):
        self.conn.close()

db=DB()
sql = 'Insert into Students values(NULL,%s,%s,%s,%s);',('Dragu','Vio',88888,12)
print(sql)
db.query(sql)
db.commit()


import MySQLdb

db=('127.0.0.1', 'root','ioana','ClassBook')

class DB:
    conn=None
    def connect(self):
        self.conn=MySQLdb.connect(host=db[0], user=db[1], passwd=db[2], db=db[3])


    def cursor(self):
        cursor=self.conn.cursor()
        return cursor

    def commit(self):
        return self.conn.commit()

    def close(self):
        self.conn.close()




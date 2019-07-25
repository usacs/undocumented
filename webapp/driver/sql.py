import pymysql
import config as config


class SQL:
    conn = None
    def connect(self):
        """
            Connects to the databse
        """
        connection = pymysql.connect(host = config.host, user = config.username,password = config.password,db  = 'data',cursorclass = pymysql.cursors.DictCursor)
        self.conn = connection
    def SelectQuery(self,query:str,x = None,one:bool = True)->dict:
        """
            Returns a SELECT  query, default is fetchOne , but specify one = False to fetchAll
        """
        conn = self.conn
        if conn == None:
            print("Connection not setup yet, Please connect!")
            return None
        with conn.cursor() as cursor:
            cursor.execute(query,x)
            return cursor.fetchone() if one else cursor.fetchall()

    def InsertQuery(self,query:str, x):
        """
            Makes an INSERT Query
        """
        conn = self.conn
        if conn == None:
            print("Connection not setup yet, Please connect!")
            return None
        with conn.cursor() as cursor:
            cursor.execute(query,x)
        conn.commit()

    def ExecuteRaw(self,query, fetch_one=False):
        conn = self.conn
        if conn == None:
            print("Connection not setup yet, Please connect!")
            return None
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return cursor.fetchone() if fetch_one else cursor.fetchall()

import psycopg2 as psycopg2


class DbConfig:
    def __init__(self, host,username, password,port,dbname):
        self.host=host
        self.password=password
        self.port=port
        self.username=username
        self.dbname=dbname
    def getConnection(self):
        print("get conection")
        conn = psycopg2.connect(database=self.dbname, user=self.username, password=self.password, host=self.host)
        return conn

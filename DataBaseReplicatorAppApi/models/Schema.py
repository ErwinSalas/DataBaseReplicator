class Schema:
    def __init__(self, name, connection):
        self.name = name
        self.tables = self.getTables()
        self.views=self.getTables()
        self.connection = connection

    def getTables(self):
        list = []
        cur = self.connection.cursor()
        cur.execute(str.format("select * from information_schema.tables where table_schema = %s " , self.name))
        result = cur.fetchall()
        for element in result:
            print(element)

        cur.close()

    def getViews(self):
        list = []
        cur = self.connection.cursor()
        cur.execute(str.format("select * from information_schema.views where table_schema = %s " , self.name))
        result = cur.fetchall()
        for element in result:
            print(element)

        cur.close()
class Schema:
    def __init__(self, name, connection):
        self.name = name
        self.connection = connection
        self.tables = self.getTables()
        #self.views=self.getTables()

    def getTables(self):
        list = []
        cur = self.connection.cursor()
        print("-------------", self.name)
        cur.execute("select * from information_schema.tables where table_schema = '%s'" % ( self.name))
        result = cur.fetchall()
        for element in result:
            list.append(element[2])
        cur.close()
        return list

    def getViews(self):
        list = []
        cur = self.connection.cursor()
        cur.execute("select * from information_schema.views where table_schema = %s" % (self.name))
        result = cur.fetchall()
        for element in result:
            print(element)

        cur.close()
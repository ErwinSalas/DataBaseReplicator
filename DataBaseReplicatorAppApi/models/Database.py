class Database:
    def __init__(self, name, size,connection):
        self.name=name
        self.size=size
        self.schemas=self.getSchemas()
        self.connection=connection

    def getSchemas(self):
        list = []
        cur = self.connection.cursor()
        cur.execute("SELECT n.nspname FROM pg_namespace n;")
        result = cur.fetchall()
        for element in result:
            print(element)

        cur.close()



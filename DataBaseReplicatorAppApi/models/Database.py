from models.Schema import Schema


class Database:
    def __init__(self, name,connection):
        self.name = name
        self.connection = connection
        self.schemas = self.getSchemas()
        print("database")

    def getSchemas(self):
        list = []
        cur = self.connection.cursor()
        cur.execute("SELECT n.nspname FROM pg_namespace n;")
        result = cur.fetchall()
        for element in result:
            print(element)
            schema=Schema(element[0],self.connection)
            list.append(schema)

        cur.close()
        return list



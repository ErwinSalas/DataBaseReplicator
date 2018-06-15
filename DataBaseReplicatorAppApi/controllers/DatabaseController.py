from models.Database import Database
from models.DbConfig import DbConfig
from state.Status import Status


class DatabaseController:
    def __init__(self):
        print("haciendo database controller")
        pass

    def createDatabase(self, config):
        cur = config.getConnection().cursor()
        cur.execute("CREATE DATABASE '%s' " % (Status().OriginalDB.name))
        cur.close()

    def copyTables(self,config,tables):
        print("tables --------", tables)
        cur = config.getConnection().cursor()
        for table in tables:
            cur.execute("select createTable('%s','%s','%s','%s','%s','%s') " %(table,config.host,config.port,config.dbname,config.username,config.password))
            print("for---", table)
        print("listo copy tables")
        cur.close()

    def conectOriginal(self,content,db_type):
        config = DbConfig(
            content["host"],
            content["username"],
            content["password"],
            content["port"],
            content["dbname"]
        )
        print("1111111111111")
        db = Database(content["dbname"], config.getConnection())
        status = Status()
        if (db_type==1):
            status.OriginalDB = db
        elif (db_type==2):
            status.CopyDB = db

    #metodo para crear los trigers


    #metodo para copiar parcial


    #metodo para obtener base de datos


from models.Database import Database
from models.DbConfig import DbConfig
from state.Status import Status


class DatabaseController:
    def __init__(self):
       pass

    def copyAllDataBase(self,config):
        cur = config.getConnection().cursor()
        cur.execute(str.format("CREATE DATABASE new WITH TEMPLATE %s",Status.OriginalDB.name))
        cur.close()

    def conectOriginal(self,content,db_type):
        config = DbConfig(
            content["host"],
            content["username"],
            content["password"],
            content["port"],
            content["dbname"]
        )
        db = Database(content["dbname"], config.getConnection())
        status = Status()
        if (db_type==1):
            status.OriginalDB = db
        elif (db_type==2):
            status.CopyDB = db

    #metodo para crear los trigers


    #metodo para copiar parcial


    #metodo para obtener base de datos


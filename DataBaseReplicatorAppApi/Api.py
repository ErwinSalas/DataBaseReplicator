from controllers.DatabaseController import DatabaseController
from models.Database import Database
from models.DbConfig import DbConfig
from state.Status import Status

__author__ = 'Erwin'
from flask import Flask,request,render_template

app = Flask(__name__)
app.secret_key = 'admin'

controller=DatabaseController()

@app.route('/connect/<db>', methods=['POST'])
def connect(db):
   controller.conectOriginal(request.json,db)

@app.route('/sendTables', methods=['POST'])
def setTables():
    print("sendTables")
    print("JSON---",request)
    host = str(request).split("&")
    ipSplit = host[0].split("?")
    ipAddress = ipSplit[1].split("=")
    port = host[1].split("=")
    dbname = host[2].split("=")
    username = host[3].split("=")
    password = host[4].split("=")

    ipAddress = str(ipAddress[1])
    port = str(port[1])
    dbname = str(dbname[1])
    username = str(username[1])
    password = str(password[1])

    print("/n host[0]===ipAddress====", ipAddress)
    print("host[1]===port====", port)
    print("host[2]===dbname====", dbname)
    print("host[3]====username===", username)
    print("host[4]===password====", password)

    info = host[-1].split("'")
    info2 = info[0].split(",")
    print("-.-.-.-222.-.-.-.-.-   ",info2)

    global controller
    print("estoy en setTables")

    tables=info2

    print("tb",tables)

    config = DbConfig(
        ipAddress,
        username,
        password,
        port,
        dbname
    )
    print("config creado--ip address = ", config.host)
    status=Status()

    config2=DbConfig(
        ipAddress,
        username,
        password,
        port,
        status.OriginalDB.name
    )
    db = Database(status.OriginalDB.name, config2.getConnection())
    status.CopyDB = db
    print("terminando set tables----",config, "tables", tables)
    controller.createDatabase(config)
    controller.copyTables(config2,tables)
    print("set tables listo!!")



@app.route('/index', methods=['POST'])
def index():
    config = DbConfig(
        request.form["host"],
        request.form["username"],
        request.form["password"],
        request.form["port"],
        request.form["dbname"]
    )
    db = Database(config.dbname, config.getConnection())
    status = Status()
    status.OriginalDB = db
    status.DBName = db.name

    return render_template('index.html', database = db)

@app.route('/log')
def log():
    return render_template('log.html')



@app.route('/')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
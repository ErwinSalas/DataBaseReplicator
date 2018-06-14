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

@app.route('/getAllDatabase', methods=['GET'])
def getDataBase(db):
    pass


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

    return render_template('index.html', database = db)


@app.route('/')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
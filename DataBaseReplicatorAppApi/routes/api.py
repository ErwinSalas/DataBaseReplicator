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






if __name__ == '__main__':
    app.run(debug=True)
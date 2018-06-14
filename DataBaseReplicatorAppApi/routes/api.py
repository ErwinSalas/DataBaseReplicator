__author__ = 'Erwin'
from flask import Flask,request,render_template

app = Flask(__name__)
app.secret_key = 'admin'



@app.route('/connect')
def connect():
   content =request.json




@app.route('/test/crecimiento')
def test_crecimiento():
   return render_template('test_inserts.html')



@app.route('/test/configs', methods=['POST'])
def getTestConfigs():
    connections = int(request.form['connections'])
    time = int(request.form['time'])
    operations = int(request.form['operation_number'])
    conection = DBController.DBController('centralDB', 'postgres', 'aniram', 'localhost')
    ob = Objects.Configs(connections,time ,operations)
    conection.connection(ob)
    return render_template('test_result.html', results=conection.connection(ob))


if __name__ == '__main__':
    app.run(debug=True)
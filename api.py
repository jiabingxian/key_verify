from flask import Flask,request
import json,data
app = Flask(__name__)
@app.route('/key',methods=['GET','POST'])
def key():
    card = request.values.get('card')
    d = json.dumps(data.if_key(card,turpe=True),ensure_ascii=False)
    return d,200
@app.route('/add',methods=['GET','POST'])
def add():
    name = request.values.get('name')
    y = request.values.get('y')
    m = request.values.get('m')
    n = request.values.get('n')
    n1=data.add(name,y,m,n)
    da={'key':n1}
    d = json.dumps(da,ensure_ascii=False)
    return d,200

app.run(host='127.0.0.1',port=8080)

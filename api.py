from flask import Flask,request
import json
from main import Card 
app = Flask(__name__)
@app.route('/verify',methods=['GET','POST'])
def verify():
    card = request.values.get('card')
    c=Card("",0,0,0,0)
    c.decode(card)
    info=c.info()
    d={'flag':True,'info':info}
    return json.dumps(d,ensure_ascii=False),200
@app.route('/calc',methods=['GET','POST'])
def calc():
    name = request.values.get('name')
    y = request.values.get('y')
    m = request.values.get('m')
    d = request.values.get('d')
    id = request.values.get('id')
    c=Card(name,int(id),int(y),int(m),int(d))
    d={'flag':True,'key':c.encode()}
    return json.dumps(d,ensure_ascii=False),200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
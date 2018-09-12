from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def hello():
    name = request.args.get('name', 'Flask')
    return '<h1>Hello,%s!</h1>' % name
# 设置监听HTTP的方法;
@app.route('/cxz',methods=['GET','POST'])
def cxz():
    return '<h1>Hello,Cuixiaozhao!</h1>'
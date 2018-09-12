from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def hello():
    name = request.args.get('name', 'Flask')
    return '<h1>Hello,%s!</h1>' % name


# 设置监听HTTP的方法;
@app.route('/cxz', methods=['GET', 'POST'])
def cxz():
    return '<h1>Hello,Cuixiaozhao!</h1>'


# URL处理;

@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d</p>' % (2018 - year)


# @app.route('/colors/<any(blue, white, red):color>')
# def three_colors(color):
#     return '<p>Love is patient and kid.Love is not jealous or boastful or proud or rude.</p>'


colors = ['blue', 'white', 'red']


@app.route('/colors/<any(%s):color>' % str(colors)[1:-1])
def colors(color):
    return 'woaini!'

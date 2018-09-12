from flask import Flask

app = Flask(__name__)


# 指定状态码返回;
@app.route('/code')
def code():
    return 'HTTP Response Status Codes', 201


@app.route('/tqtl')
def tqtl():
    return 'Tel:13811221893', 302, {'location', 'http://www.baidu.com'}

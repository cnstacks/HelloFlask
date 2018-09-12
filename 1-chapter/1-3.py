from flask import Flask

app = Flask(__name__)


@app.route('/greet/<name>')
def say_hello(name):
    return '<h1>Say Hello to the World!%s</h1>' % name


@app.route('/hi', defaults={'name': 'Programmer'})
@app.route('/hi/<name>')
def hi(name):
    return '<h1>Hello,%s!</h1>' % name

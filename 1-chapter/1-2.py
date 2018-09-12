from flask import Flask

app = Flask(__name__)


@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Say Hello to the World!</h1>'

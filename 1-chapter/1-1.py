from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Flask!Cuixiaozhao，To be a better programmer.</h1>'

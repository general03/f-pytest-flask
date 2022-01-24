from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/other")
def hello_other():
    return "<p>Hello, Other!</p>"


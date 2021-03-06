from flask import Flask, request
import requests

app = Flask(__name__)
# To manage the exception in pytest
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/other")
def hello_other():
    page = request.args.get('page', default = 1, type = int)
    return f"<p>Hello, Other!</p><p>Page : {page}</p>"

@app.route("/exp")
def exp():
    # ValueError throw if str is pass to value param
    value = int(request.args.get('value'))
    return f"<p>Exposant 2 de {value} : {pow(value, 2)}</p>"

@app.route("/coincoin")
def coincoin():
    response = requests.get('https://random-d.uk/api/random')
    img = response.json().get('url')
    return f"<img src='{img}' />"
from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def index():
    return 'Hola Mundo'

@app.route("/chau")
def index():
    return 'Chau'

app.run
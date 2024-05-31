from flask import Flask

app = Flask(__name__)

@app.route('/hola/')
def hola():
    return 'Hola Mundo'

@app.route('/saludo', defaults={'name': None})
@app.route('/saludo/<name>')
def saludo(name):
    return 'Hola ' + name

@app.route('/chau/')
def chau():
    return 'Chau'

if __name__ == '__main__':  
   app.run()
from flask import Flask

app = Flask(__name__)

@app.route('/hola/')
def hola():
    return 'Hola Mundo'

@app.route('/saludo', defaults={'name': None})
@app.route('/saludo/<name>')
def saludo(name):
    return 'Hola ' + name

@app.route('/nombreCompleto', defaults={'name': None, 'lastname': None})
@app.route('/nombreCompleto/<name>/<lastname>')
def nombreCompleto(name, lastname):
    return f'Hola {name} {lastname}'

@app.route('/chau/')
def chau():
    return 'Chau'

if __name__ == '__main__':  
   app.run()
from random import randint

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'

socket_io = SocketIO(app)


# Suceptible a cambios
@app.route('/')
def index():
    return render_template('index.html')


@socket_io.on('message')
def escucha(numero):
    print('Numero: ', numero)
    valor_random = randint(10, 100)
    if valor_random == numero:
        valor_random = randint(10, 100)
    send(str(valor_random), broadcast = True)


if __name__ == '__main__':
    socket_io.run(app)

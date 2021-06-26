from flask import Flask
from flask_socketio import SocketIO, send
import pymongo


app = Flask(__name__)
socket_io = SocketIO(app)

@app.route('/')
def hello():
    client = pymongo.MongoClient("mongodb+srv://new_user:sikuani@cluster0.vxniy.mongodb.net/sikuanidb?retryWrites=true&w=majority") 
    db = client.test
    return str(db)

# Suceptible a cambios
#@app.route('/')
#def index():
#    return render_template('index.html')


@socket_io.on('message')
def escucha(numero):
    print('Numero: ', numero)
    valor_random = randint(10, 100)
    if valor_random == numero:
        valor_random = randint(10, 100)
    send(str(valor_random), broadcast = True)

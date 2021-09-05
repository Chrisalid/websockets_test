from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
ws = SocketIO(app)

messages = []


@app.route('/')
def home():
    return render_template('index.html')


@ws.on('sendMessage')
def send_message_handler(msg):
    messages.append(msg)
    emit('getMessage', msg, broadcast=True)


@ws.on('message')
def message_handler(msg):
    send(messages)


if __name__ == '__main__':
    ws.run(app, debug=True)

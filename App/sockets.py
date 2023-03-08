from flask_socketio import (
    SocketIO, send, emit, join_room, leave_room
)
from .models.message import Message

socketio = SocketIO()


@socketio.on("message")
def handle_message(message):
    Message(contents=message).add()
    send(message, broadcast=True)


@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    print("join")
    join_room(room)
    send(username + ' has entered the room.', to=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    print("left")
    leave_room(room)
    send(username + ' has left the room.', to=room)

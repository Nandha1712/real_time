import uuid
from flask_socketio import SocketIO, emit
from flask import Flask, session, request

app = Flask(__name__)

ORIGINS = "*"

# initialize your socket instance
socketio = SocketIO(cors_allowed_origins=ORIGINS)


@socketio.on('connect')
def events_connect():
    print(f"Connected....{request.sid}")


@app.route('/update/<req_id>/<custom_msg>')
def post_custom_msg(req_id, custom_msg):
    n_msg = {"user": "New", "msg": custom_msg}
    socketio.emit("chat", n_msg, to=req_id)
    return "Data pushed"

# handle chat messages
@socketio.on("chat")
def handle_chat(data):
    print(f"Incoming data...{data}")
    print(f"inside chat....{request.sid}")
    """Char func

    Args:
        data (_type_): _description_
    """
    emit("chat", data, to=request.sid)



# initialize the app with the socket instance
# you could include this line right after Migrate(app, db)
socketio.init_app(app)

# at the bottom of the file, use this to run the app
if __name__ == '__main__':
    app.run(debug=True)


import uuid
from flask_socketio import SocketIO, emit
from flask import Flask, session, request
from log_utils import create_logger

logger = create_logger()

app = Flask(__name__)

ORIGINS = "*"

# initialize your socket instance
socketio = SocketIO(cors_allowed_origins=ORIGINS, engineio_logger=True, logger=True)


@socketio.on('connect')
def events_connect():
    logger.error(f"Connected....{request.sid}")
    logger.error(f"Request data....{request}, {request.args.get('foo')}, {request.args}")


@app.route('/update/<req_id>/<custom_msg>')
def post_custom_msg(req_id, custom_msg):
    logger.error(f"Incoming Req id: {req_id}, Msg: {custom_msg}")
    n_msg = {"user": "New", "msg": custom_msg}
    socketio.emit("chat", n_msg, to=req_id)
    return "Data pushed"

# handle chat messages
@socketio.on("chat")
def handle_chat(data):
    logger.error(f"Incoming data...{data}")
    logger.error(f"inside chat....{request.sid}")
    """Char func

    Args:
        data (_type_): _description_
    """
    emit("chat", data, to=request.sid)


@socketio.on('disconnect')
def socket_disconnect_handler():
    logger.error(f'Client disconnected...{request.sid}')


@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    logger.error(f'Socket error...{e}')
    logger.error(f'Request SID of error...{request.sid}')


# initialize the app with the socket instance
# you could include this line right after Migrate(app, db)
socketio.init_app(app)

# at the bottom of the file, use this to run the app
if __name__ == '__main__':
    app.run(debug=True)


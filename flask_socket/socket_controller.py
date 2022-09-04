import uuid
from flask_socketio import SocketIO, emit
from flask import Flask, session, request
from log_utils import create_logger
import json

logger = create_logger()

ORIGINS = "*"

# initialize your socket instance
socketio = SocketIO(cors_allowed_origins=ORIGINS, engineio_logger=True, logger=True)


@socketio.on('connect')
def events_connect():
    req_sid = request.sid
    logger.error(f"Connected....{req_sid}")

    user_id = str(request.args.get('user_id'))

    userdata = session.get(user_id)
    if userdata is None:
        session[user_id] = req_sid
        logger.error(f"Setting userdata....{req_sid}, {user_id}")

    data = None
    with open('res_dict.json', 'r') as f:
        data = json.load(f)
    
    data[user_id] = req_sid
    with open('res_dict.json', 'w') as json_file:
        json.dump(data, json_file)

    logger.error(f"Request data....{request}, {user_id}")



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

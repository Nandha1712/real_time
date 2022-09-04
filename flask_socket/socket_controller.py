import uuid
from flask_socketio import SocketIO, emit
from flask import Flask, session, request
from log_utils import create_logger

logger = create_logger()

ORIGINS = "*"

# initialize your socket instance
socketio = SocketIO(cors_allowed_origins=ORIGINS, engineio_logger=True, logger=True)


@socketio.on('connect')
def events_connect():
    logger.error(f"Connected....{request.sid}")
    logger.error(f"Request data....{request}, {request.args.get('foo')}, {request.args}")



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

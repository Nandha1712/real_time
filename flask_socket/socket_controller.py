from operator import le
import uuid
from flask_socketio import SocketIO, emit
from flask import Flask, session, request
from log_utils import create_logger
import json
import os
from cache import get_cache_value, set_cached_item, delete_cached_item

logger = create_logger()

ORIGINS = "*"

# initialize your socket instance
socketio = SocketIO(cors_allowed_origins=ORIGINS, engineio_logger=True, logger=True)


@socketio.on('connect')
def events_connect():
    req_sid = request.sid
    current_process_id = os.getpid()
    logger.error(f"PID: {current_process_id} Socket Connected....{req_sid}")

    user_id = str(request.args.get('user_id'))
    user_data = get_cache_value(user_id)
    if user_data is None:
        user_data = []
    
    user_data.append(req_sid)

    set_cached_item(str(user_id), user_data)
    set_cached_item(req_sid, f"{user_id}")

    logger.error(f"PID:{current_process_id} Request data. {request}, User: {user_id}, {req_sid}")



# handle chat messages
@socketio.on("chat")
def handle_chat(data):
    logger.error(f"PID: {os.getpid()} inside chat....{request.sid}")
    """Char func

    Args:
        data (_type_): _description_
    """
    emit("chat", data, to=request.sid)


@socketio.on('disconnect')
def socket_disconnect_handler():
    current_process_id = os.getpid()
    req_sid = request.sid

    user_id_key = get_cache_value(req_sid)
    delete_cached_item(req_sid)
    
    if user_id_key is None:
        return

    user_data = get_cache_value(user_id_key)
    if user_data is None or req_sid not in user_data:
        return
    
    user_data.remove(req_sid)

    set_cached_item(user_id_key, user_data)
    
    logger.error(f'PID: {current_process_id} Client disconnected...{req_sid}')


@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    logger.error(f'PID: {os.getpid()} Request SID of error...{request.sid} Socket error...{e} ')


import uuid
import json

from flask import Blueprint, session, jsonify, request
from log_utils import create_logger
from socket_controller import socketio
import os
from cache import get_cache_value

logger = create_logger()

ws_api = Blueprint('app', __name__)


@ws_api.route('/update/<user_id>/<custom_msg>')
def post_custom_msg(user_id, custom_msg):
    current_process_id = os.getpid()
    logger.error(f"pid....{current_process_id}")

    user_data = get_cache_value(user_id)

    if user_data is None:
        logger.error(f"user_data is None from cache")
        return jsonify({"message": "Incorrect user id"})

    for req_id in user_data:
        logger.error(f"Incoming Req id: {req_id}, Msg: {custom_msg}")
        n_msg = {"user": "New", "msg": custom_msg}
        socketio.emit("chat", n_msg, to=req_id)
    
    return jsonify({"message": "pushed"})


@ws_api.route('/print_cache')
def print_cache_data():
    current_process_id = os.getpid()
    from cache import cache_app
    
    logger.error(f"pid....{current_process_id}, {cache_app}")

    return jsonify({"message": "printed"})

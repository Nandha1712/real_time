import uuid
import json

from flask import Blueprint, session, jsonify, request
from log_utils import create_logger
from socket_controller import socketio

logger = create_logger()

ws_api = Blueprint('app', __name__)


@ws_api.route('/update/<user_id>/<custom_msg>')
def post_custom_msg(user_id, custom_msg):
    with open('res_dict.json', 'r') as f:
        data = json.load(f)
        req_id = data.get(str(user_id))
        logger.error(f"JSON res is {req_id}")
    
    userdata = session.get(user_id)
    if userdata is None:
        logger.error(f"userdata is None from session")
    
    if req_id is None:
        logger.error(f"Reqid is None")
        return "Incorrect user id"

    logger.error(f"Incoming Req id: {req_id}, Msg: {custom_msg}")
    n_msg = {"user": "New", "msg": custom_msg}
    socketio.emit("chat", n_msg, to=req_id)
    return "Data pushed"

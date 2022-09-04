import uuid

from flask import Blueprint, session, jsonify, request
from log_utils import create_logger
from socket_controller import socketio

logger = create_logger()

ws_api = Blueprint('app', __name__)


@ws_api.route('/update/<req_id>/<custom_msg>')
def post_custom_msg(req_id, custom_msg):
    logger.error(f"Incoming Req id: {req_id}, Msg: {custom_msg}")
    n_msg = {"user": "New", "msg": custom_msg}
    socketio.emit("chat", n_msg, to=req_id)
    return "Data pushed"

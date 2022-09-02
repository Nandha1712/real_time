import uuid
from flask_socketio import SocketIO, emit
from flask import Flask, session, request
import logging

logger = logging.getLogger("app_log")
logger.setLevel(logging.INFO)

app = Flask(__name__)

ORIGINS = "*"

# initialize your socket instance
socketio = SocketIO(cors_allowed_origins=ORIGINS, engineio_logger=True, logger=True)


@socketio.on('connect')
def events_connect():
    logger.error(f"Connected....{request.sid}")


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



# initialize the app with the socket instance
# you could include this line right after Migrate(app, db)
socketio.init_app(app)

# at the bottom of the file, use this to run the app
if __name__ == '__main__':
    app.run(debug=True)


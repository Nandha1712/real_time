import uuid
from flask_socketio import SocketIO, emit
from flask import Flask, session, request
from log_utils import create_logger
from api_controller import ws_api
from socket_controller import socketio
logger = create_logger()

app = Flask(__name__)

# initialize the app with the socket instance
# you could include this line right after Migrate(app, db)
socketio.init_app(app)

app.register_blueprint(ws_api)

# at the bottom of the file, use this to run the app
if __name__ == '__main__':
    app.run()


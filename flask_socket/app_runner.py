from flask import Flask
from log_utils import create_logger
from api_controller import ws_api
from socket_controller import socketio
from flask_session import Session

logger = create_logger()

app = Flask(__name__)

session_app = Session()

# initialize the app with the socket instance
# you could include this line right after Migrate(app, db)
socketio.init_app(app)

session_app.init_app(app)

app.register_blueprint(ws_api)

app.config['SESSION_TYPE'] = 'filesystem'

# at the bottom of the file, use this to run the app
if __name__ == '__main__':
    app.run()


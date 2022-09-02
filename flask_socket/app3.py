from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/")
def index():
    print("root route...")
    return "ttt"


@socketio.on('connect', namespace='/test')
def my_event(message):
    print(f"Inside my event - {message}")
    emit("my response", {"data": "got it!"})


if __name__ == "__main__":
    socketio.run(app)

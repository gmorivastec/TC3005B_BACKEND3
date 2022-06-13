from flask import Flask, render_template
from flask_sock import Sock
from flask_cors import CORS
import sys

app = Flask(__name__)
sock = Sock(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def root():
    return render_template('index.html')


@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        print(data, file=sys.stdout)
        sock.send(data)

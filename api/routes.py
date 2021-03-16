from api import app
from board import main
from flask import request
from flask import jsonify
# import json
b = main.Board()

@app.route('/')
@app.route('/index')
def index():
    print(b.get_board())
    return "Hello World"

@app.route('/fen', methods=['POST'])
def init_fen():
    # data = json.loads(request.json)
    data = request.json
    print(data)
    if data['fen']:
        fen = data['fen']
        print(fen)
        b.init_fen(fen)
        return "Init from FEN: {}".format(fen)
    return "Couldn't find a FEN"

@app.route('/board')
def get_board():
    return b.get_json()

@app.route('/move/<string:move>')
def process_move(move):
    b.process_move(move)
    return b.get_json()

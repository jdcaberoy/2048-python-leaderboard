from app import app
from flask import request, redirect, url_for, jsonify, render_template


@app.route('/')
@app.route('/index')
def index():
    # render_template('index.html')
    return "Hello, World!"

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        # content = request.get_json()
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        # Extract the values from the JSON data
        player = data.get('player')
        score = data.get('score')
        passing = data.get('passing')
        print(player, score, passing)
        if not player or not isinstance(score, int) or passing is None:
            return jsonify({'error': 'Invalid data format'}), 400
        return jsonify({'message': 'Results processed successfully'}), 200

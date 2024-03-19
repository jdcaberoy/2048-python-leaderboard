from app import app
from flask import request, redirect, url_for, jsonify, render_template
import pandas as pd
import os
from datetime import datetime


# Define the file path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(ROOT_DIR, 'Results')
RESULTS_FILE = os.path.join(RESULTS_DIR, '2048_results_test.xlsx')

# Create the Results directory if it doesn't exist
os.makedirs(RESULTS_DIR, exist_ok=True)

def write_results(player, score, passing):

    if os.path.isfile(RESULTS_FILE):
        df = pd.read_excel(RESULTS_FILE)
    else:
        df = pd.DataFrame(columns=['Index', 'Time', 'Player', 'Score', 'Passing'])

    new_result = pd.DataFrame({
        'Index': [len(df) + 1],
        'Time': [datetime.now()],
        'Player': [player],
        'Score': [score],
        'Passing': [passing]
    })
    df = pd.concat([df, new_result], ignore_index=True)

    # Save the DataFrame to the Excel file
    df.to_excel(RESULTS_FILE, index=False)

@app.route('/')
@app.route('/index')
def index():
    # render_template('index.html')
    return "Hello, World!"

@app.route('/results', methods=['GET', 'PUT'])
def results():
    if request.method == 'PUT':
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
        write_results(player, score, passing)
        return jsonify({'message': 'Results processed successfully'}), 200
    if request.method == 'GET':
        return jsonify({'message': 'not yet implemented'}), 404

from flask import Flask, jsonify
from flask_cors import CORS
import json
from pokemon_data import get_pokemon

app = Flask(__name__)
CORS(app)
@app.route('/call_results', methods=['GET'])

def call_results():
    try:
        results = get_pokemon()
        pokejson = json.dumps(results.__dict__)
        return pokejson
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
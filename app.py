from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage (for demonstration purposes)
data_store = []

# Endpoint to handle POST requests
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    # Store the posted data
    data_store.append(data)
    
    return jsonify({'message': 'Data received successfully', 'data': data}), 200

# Endpoint to get all posted data
@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({'data': data_store}), 200

# Endpoint to handle DELETE requests by Load ID
@app.route('/delete_data', methods=['DELETE'])
def delete_data():
    load_id = request.args.get('load_id')  # Get the Load ID from query parameters
    if not load_id:
        return jsonify({'error': 'Load ID not provided'}), 400
    
    global data_store
    initial_len = len(data_store)
    data_store = [item for item in data_store if item.get('Load ID') != load_id]
    
    if len(data_store) == initial_len:
        return jsonify({'error': 'Load ID not found'}), 404
    
    return jsonify({'message': 'Data deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

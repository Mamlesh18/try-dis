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

# Endpoint to handle DELETE requests
@app.route('/delete_data', methods=['DELETE'])
def delete_data():
    # Clear all data
    data_store.clear()
    return jsonify({'message': 'All data deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store client data
clients = {}

@app.route('/register', methods=['POST'])
def register_client():
    data = request.get_json()
    if 'client_id' not in data:
        return jsonify({'error': 'Invalid request. Missing client_id.'}), 400

    client_id = data['client_id']
    clients[client_id] = {'commands': []}
    return jsonify({'message': f'Registered client with ID: {client_id}'}), 200

@app.route('/command', methods=['POST'])
def get_command():
    data = request.get_json()
    if 'client_id' not in data:
        return jsonify({'error': 'Invalid request. Missing client_id.'}), 400

    client_id = data['client_id']
    if client_id not in clients:
        return jsonify({'error': 'Unknown client ID. Register first.'}), 404

    if not clients[client_id]['commands']:
        return jsonify({'message': 'No commands at the moment.'}), 200

    command = clients[client_id]['commands'].pop(0)
    return jsonify({'command': command}), 200

@app.route('/response', methods=['POST'])
def send_response():
    data = request.get_json()
    if 'client_id' not in data or 'response' not in data:
        return jsonify({'error': 'Invalid request. Missing client_id or response.'}), 400

    client_id = data['client_id']
    response = data['response']
    if client_id not in clients:
        return jsonify({'error': 'Unknown client ID. Register first.'}), 404

    clients[client_id]['responses'] = response
    return jsonify({'message': 'Response received successfully.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

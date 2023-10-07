from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__)

# Configure JWT settings
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

# Mock user data (replace with your user database)
users = {
    'user1': {'password': 'password1', 'role': 'user'},
    'admin': {'password': 'adminpassword', 'role': 'admin'}
}

# Authentication endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users or users[username]['password'] != password:
        return jsonify({"message": "Invalid credentials"}), 401

    # Create a JWT token with user identity and claims
    access_token = create_access_token(identity={'username': username, 'role': users[username]['role']})
    return jsonify({"access_token": access_token}), 200

# Protected endpoint
@app.route('/protected', methods=['GET'])
@jwt_required()  # Requires a valid JWT token
def protected():
    current_user = get_jwt_identity()
    role_claim = current_user.get('role') if current_user else None
    return jsonify({"message": "This is a protected endpoint",
                    "user": current_user,
                    "role": role_claim}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)

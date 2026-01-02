#!/usr/bin/python3
"""This module implements API security with Basic Auth and JWT."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key for JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# In-memory user storage
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic auth."""
    if username in users:
        if check_password_hash(users[username]['password'], password):
            return username
    return None


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle fresh token required."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Protected route using basic authentication."""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login route that returns a JWT token."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid credentials"}), 401

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create token with user identity and role
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]['role']}
    )

    return jsonify({"access_token": access_token})


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Protected route using JWT authentication."""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Protected route for admin users only."""
    claims = get_jwt()
    role = claims.get('role')

    if role != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()

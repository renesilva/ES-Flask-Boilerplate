from flask import jsonify, Blueprint, request
from dotenv import load_dotenv
import os
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

jwt_auth_bp = Blueprint('jwt_auth_bp', __name__, url_prefix='/jwt-auth')
load_dotenv()


@jwt_auth_bp.route('/test-connection', methods=['GET'])
def route_test_connection():
    return jsonify({'message': 'Connection Successful from JWT Auth'})


@jwt_auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username == os.getenv('USER_JWT_1') and password == os.getenv('PASSWORD_JWT_1'):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid credentials"}), 401


@jwt_auth_bp.route('/test-jwt-protected', methods=['GET'])
@jwt_required()
def route_test_jwt_protected():
    current_user = get_jwt_identity()
    return jsonify({
        'message': 'Connection Successful from Eresea AI with JWT',
        'current_user': current_user,
    })

from flask import jsonify, Blueprint, request

from app.auth.basic_auth.basic_auth import basic_auth_auth

test_bp = Blueprint('test_bp', __name__, url_prefix='/test')


@test_bp.route('/test-auth', methods=['GET'])
@basic_auth_auth.login_required
def route_test_auth():
    return jsonify({'message': 'You are authenticated'})

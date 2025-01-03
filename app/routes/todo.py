from flask import jsonify, Blueprint

from app.models.todo import ToDo

todo_bp = Blueprint('todo_bp', __name__, url_prefix='/todo')


@todo_bp.route('/tasks', methods=['GET'])
def route_test_auth():
    tasks_query = ToDo.query.all()
    tasks = [task.as_dict() for task in tasks_query]
    return jsonify({'tasks': tasks})

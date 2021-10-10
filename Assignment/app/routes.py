from flask import request, jsonify
from app import app
from app import database as db_helper


"""@app.route("/delete/<int:task_id>", methods=['DELETE'])
def delete(task_id):
    try:
        db_helper.remove_task_by_id(task_id)
        result = {
            'status': 200,
            'response': 'Removed task'
        }

    except Exception as Err:
        result = {
            'status': 404,
            'response': str(Err)
        }

    return jsonify(result)"""


@app.route("/api/v1/todo", methods=['UPDATE'])
def update(task_id):
    data = request.get_json()
    print(data)
    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/api/v1/todo", methods=['POST'])
def create():
    data = request.get_json()
    db_helper.insert_data(data['description'])
    try:
        result = {
            'status': 200,
            'response': 'Data inserted succesfully'
        }
    except Exception as Err:
        result = {
            'status': 404,
            'response': str(Err)
        }
    return jsonify(result)


@app.route("/")
def homepage():
    items = db_helper.fetch_todo()

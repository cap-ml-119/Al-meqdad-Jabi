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


@app.route("/api/v1/todo/<Data_ID>", methods=['PUT'])
def update(Data_ID):
    Test = db_helper.Get_Data()
    try:
        data = request.get_json()
        db_helper.update_data(Data_ID, data["description"], data["status"])
        result = {
            "success": 200,
            "response": "Data was updated succefully"
        }
    except Exception as err:
        result = {
            'status': 404,
            'response': str(err)
        }

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


@app.route("/api/v1/todo/", methods=["GET"])
def GetAllData():
    try:
        result = db_helper.Get_Data()
        items = {
            "status": 200,
            "response": result
        }

    except Exception:
        items = {
            'status': 404,
            "response": str(Exception)
        }
    return jsonify(items)


@app.route("/")
def homepage():
    items = db_helper.fetch_todo()

from flask import request, jsonify
from app import app
from app import database as db_helper


@app.route("/api/v1/todo/<Data_ID>", methods=['DELETE'])
def delete(Data_ID):
    """[This api is responsible for deleting a
    segnificent row from Our list of data by using the id]

    Returns:
        [json dictionary]: [It reutrn the result of
        this api method wether it's a success by
        returning status 200 and success message
        or failuer by returning status 404 and an error message]
    """
    try:
        db_helper.DeleteDataByID(Data_ID)
        result = {
            'status': 200,
            'response': 'Removed task'
        }

    except Exception as Err:
        result = {
            'status': 404,
            'response': str(Err)
        }

    return jsonify(result)


@app.route("/api/v1/todo/<Data_ID>", methods=['PUT'])
def update(Data_ID):
    """[This api is responsible for updating the documant of a
    segnificent row from Our list of data by using the id]

    Returns:
        [json dictionary]: [It reutrn the result of
        this api method wether it's a success by
        returning status 200 and success message
        or failuer by returning status 404 and an error message]
    """

    try:
        data = request.get_json()
        db_helper.update_data(Data_ID, data["description"])
        result = {
            "status": 200,
            "response": "Data was updated succefully"
        }
    except Exception as err:
        result = {
            'status': 404,
            'response': str(err)
        }

    return jsonify(result)


@app.route("/api/v1/todo/<Data_ID>", methods=['PATCH'])
def Update_status(Data_ID):
    """[This api is responsible for updating the status in a
    segnificent row from Our
    list of data by using the id]

    Returns:
        [json dictionary]: [It reutrn the result of
        this api method wether it's a success by
        returning status 200 and success message
        or failuer by returning status 404 and an error message]
    """
    try:
        data = request.get_json()
        db_helper.update_data_status(Data_ID, data["status"])
        result = {
            "status": 200,
            "response": "The status for this data has been updated succesfully"
        }
    except Exception as err:
        result = {
            'status': 404,
            'response': str(err)
        }

    return jsonify(result)


@app.route("/api/v1/todo", methods=['POST'])
def create():
    """[This api is resbosiable for creating a list
    of data in our todo list it sends the data
    into a function in our local database]

    Returns:
        [Json Dictionary]: [in case of success it returns the
        result to the user after
        inserting the data which are the status: 200 and a response aka success
        message in case of failuer it will return status 404 and a response
        with an expetion error message]
    """

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
    """[This funtcion gets all the data from our
    todo list it sends the request to a function in our
    local database to retrive all the data]

    Returns:
        [Json dictionary]: [in case of success it returns a status of 200
        and the result which is the data retreived from the list in our local
        database in case of failuer it will
        return status 400 and and exception error]
    """
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


"""[This funtcion gets a segnificent row of data depending on the id entered]

    Returns:
        [Json dictionary]: [in case of success it returns a status of 200
        and the result which is the data retreived that matches the
        entered id from the list in our local
        database in case of failuer it will
        return status 400 and and exception error]
"""


@app.route("/api/v1/todo/<Data_ID>", methods=["GET"])
def GetDataByID(Data_ID):
    """[This funtcion gets a segnificent row of data depending on the id entered]

    Returns:
        [Json dictionary]: [in case of success it returns a status of 200
        and the result which is the data retreived that matches the
        entered id from the list in our local
        database in case of failuer it will
        return status 400 and and exception error]
    """
    try:
        result = db_helper.GetDataByID(Data_ID)
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
    return 0

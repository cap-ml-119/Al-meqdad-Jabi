from flask import request, jsonify, Blueprint
import pickle
import pandas as pd
from flask_expects_json import expects_json
from typing import Any
from io import StringIO
from werkzeug.wrappers import Response

# Creates


def Get_Data(Json_Object):
    temp_Data = []
    Object = Json_Object.keys()

    for key in Object:
        temp_Data.append(Json_Object[key])

    return temp_Data


def StringifyData(Ppddf):
    Data = []
    for X in Ppddf:
        Data.append(str(X[0])+"\n")

    return Data


Prediction_Apis: Blueprint = Blueprint(
    'Prediction_Apis', __name__, url_prefix='/api/v1')

Single_Prediction_Jsonschema = {
    "type": "object",
    "properties": {
        'season': {"type": "number"},
        'weather': {"type": "number"},
        "temp": {"type": "number"},
        'humidity': {"type": "number"},
        'windspeed': {"type": "number"},
        'hour': {"type": "number"},
        'day': {"type": "number"},

    },
    "required": ["season", "weather", "temp", "humidity",
                 "windspeed", "hour", "day"]
}

with open('./app/src/Models/model.sav', 'rb') as handle:
    model = pickle.load(handle)


@Prediction_Apis.route('/Single_Prediction', methods=['POST'])
@expects_json(Single_Prediction_JsonSchema)
def Single_Prediction():
    """[This api purpose is to predict a single line
    of data entered by the use through the json schema we created]

    Returns:
        [Prediction]: [it returns the model prediction of the target variable]
    """
    json: Any = request.get_json()
    result = {
        "Prediction": model.predict([Get_Data(json)])[0][0]
    }
    return jsonify(result)


@Prediction_Apis.route('/Patch_Prediction', methods=['POST'])
def Patch_Prediction():
    try:

        if 'Test_File' not in request.files:
            raise Exception("No File attached")
        Patch_Prediction_File = request.files['Test_File']
        Ppddf = pd.read_csv(
            StringIO(Patch_Prediction_File.stream.read().decode('utf-8')))
        Predictions = model.predict(PPF_DF)

        response = Response(StringifyData(
            Predictions), mimetype='text/csv')

    except Exception:
        response = {
            'status': 400,
            "response": "Something went wrong"
        }
    return response

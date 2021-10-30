from flask import request, jsonify, Blueprint
import pickle
import pandas as pd
from flask_expects_json import expects_json
from typing import Any
from io import StringIO
from werkzeug.wrappers import Response

# Creates


def GetData(JsonObject):
    tempData = []
    Object = JsonObject.keys()

    for key in Object:
        tempData.append(JsonObject[key])

    return tempData


def StringifyData(PPD_DF):
    Data = []
    for X in PPD_DF:
        Data.append(str(X[0])+"\n")

    return Data


PredictionApi: Blueprint = Blueprint(
    'PredictionApi', __name__, url_prefix='/api/v1')

Single_Prediction_JsonSchema = {
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


@PredictionApi.route('/SinglePrediction', methods=['POST'])
@expects_json(Single_Prediction_JsonSchema)
def SinglePrediction():
    """[This api purpose is to predict a single line
    of data entered by the use through the json schema we created]

    Returns:
        [Prediction]: [it returns the model prediction of the target variable]
    """
    json: Any = request.get_json()
    result = {
        "Prediction": model.predict([GetData(json)])[0][0]
    }
    return jsonify(result)


@PredictionApi.route('/PatchPrediction', methods=['POST'])
def PatchPrediction():
    try:

        if 'Test_File' not in request.files:
            raise Exception("No File attached")
        Patch_Prediction_File = request.files['Test_File']
        PPF_DF = pd.read_csv(
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

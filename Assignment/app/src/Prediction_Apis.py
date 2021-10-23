from flask import request, jsonify, Blueprint
import math
import pickle
import numpy as np
import pandas as pd
from flask_expects_json import expects_json
from typing import Any

# Creates


def get_json_data(obj):
    tempData = []
    obj_keys = obj.keys()

    for key in obj_keys:
        tempData.append(obj[key])

    return tempData


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
def ModelSP():
    """[This api purpose is to predict a single line
    of data entered by the use through the json schema we created]

    Returns:
        [Prediction]: [it returns the model prediction of the target variable]
    """
    json: Any = request.get_json()
    result = {
        "Prediction": model.predict([get_json_data(json)])[0][0]
    }

    return jsonify(result)

from flask import Flask, jsonify

from Prediction_Apis import PredictionApi
app = Flask(__name__)

app.register_blueprint(PredictionApi)

if __name__ == '__main__':
    app.run(host="localhost", port=9900, debug=True)

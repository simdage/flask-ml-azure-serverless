from flask import Flask
from flask.logging import create_logger
import logging
import os
import joblib
from flask import request, jsonify
from argparse import ArgumentParser

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route("/")
def home():
    html = (
        "<h3>Sklearn Prediction Home: From Azure Pipelines (Continuous Delivery)</h3>"
    )
    return html.format(format)


@app.route("/predict", methods=["POST"])
def predict():
    """
    Performs a sklearn prediction on iris dataset
    """

    clf = joblib.load("iris_prediction.joblib")
    payload = request.json
    #LOG.info("JSON payload: %s json_payload")
    print(payload)
    prediction = list(clf.predict(payload))
    prediction = [float(i) for i in prediction]
    print(prediction)
    pred = jsonify({"prediction": prediction})
    print(pred)
    #LOG.info("Prediction:", pred)
    return pred


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int)
    args = parser.parse_args()

    port = args.port
    if not args.port:
        port = 8080

    # include argument for testing in order to use different port
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", port)), debug=True)

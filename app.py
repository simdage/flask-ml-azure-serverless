from flask import Flask, redirect, url_for, render_template
from flask.logging import create_logger
import logging
import os
import joblib
from flask import request, jsonify
from argparse import ArgumentParser

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

# Replace these with your own username and password
USERNAME = 'your_username'
PASSWORD = 'your_password'


@app.route('/')
def index():
    if 'logged_in' in request.cookies and request.cookies['logged_in'] == 'true':
        return 'Welcome to your app!'
    else:
        return redirect(url_for('login'))


@app.route("/predict", methods=["POST"])
def predict():
    """
    Performs a sklearn prediction on iris dataset
    """

    clf = joblib.load("iris_prediction.joblib")
    payload = request.json
    # LOG.info("JSON payload: %s json_payload")
    print(payload)
    prediction = list(clf.predict(payload))
    prediction = [float(i) for i in prediction]
    print(prediction)
    pred = jsonify({"prediction": prediction})
    print(pred)
    # LOG.info("Prediction:", pred)
    return pred


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            resp = redirect(url_for('index'))
            resp.set_cookie('logged_in', 'true')
            return resp
        else:
            return 'Invalid credentials. Try again.'

    return render_template('login.html')


@app.route('/logout')
def logout():
    resp = redirect(url_for('login'))
    resp.set_cookie('logged_in', 'false')
    return resp


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int)
    args = parser.parse_args()

    port = args.port
    if not args.port:
        port = 8080

    # include argument for testing in order to use different port
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", port)), debug=True)

""" Devops challenge main application."""
import json
from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route("/healthcheck")
def status():
    """Route to get api status."""
    resp = {"Status": "heart beating steady and strong"}
    response = app.response_class(
        response=json.dumps(resp), status=200, mimetype="application/json"
    )
    return response


@app.route("/")
def main():
    """Api main route."""
    resp = {"App Test": "Alive"}
    response = app.response_class(
        response=json.dumps(resp), status=200, mimetype="application/json"
    )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_routes():
    return str(app.url_map), 200


@app.route("/hello", methods=["GET"])
def get_hello():
    return jsonify({"message": "Hello World!"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080, threaded=True)

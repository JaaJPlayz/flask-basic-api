import os

from dotenv import load_dotenv
from flask import Flask, jsonify

from database.database import db

load_dotenv()
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///test.db")


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

db.init_app(app)


@app.route("/", methods=["GET"])
def get_routes():
    return str(app.url_map), 200


@app.route("/hello", methods=["GET"])
def get_hello():
    return jsonify({"message": "Hello World!"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080, threaded=True)

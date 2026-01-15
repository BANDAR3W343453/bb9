from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Server OK"

@app.route("/activate", methods=["POST"])
def activate():
    data = request.get_json()
    key = data.get("key")

    with open("keys.json", "r") as f:
        keys = json.load(f)

    if key in keys:
        keys.remove(key)
        with open("keys.json", "w") as f:
            json.dump(keys, f)

        return jsonify({"status": "activated"})
    else:
        return jsonify({"status": "invalid"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

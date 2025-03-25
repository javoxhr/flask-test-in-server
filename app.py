import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API работает на Railway!"

@app.route("/data")
def get_data():
    data = {"users": ["Alice", "Bob", "Charlie"]}
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
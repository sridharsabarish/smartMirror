from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/data", methods=["POST"])
def receive_data():
    global latest_data

    data = request.get_json()
    latest_data = {
        "temperature": data.get("temperature"),
        "humidity": data.get("humidity"),
        "timestamp": datetime.now().isoformat()
    }

    print(latest_data)

    return jsonify({"status": "received"}), 200


@app.route("/data", methods=["GET"])
def send_data():
    if latest_data:
        return jsonify(latest_data), 200
    else:
        return jsonify({"message": "No data yet"}), 200


@app.route("/data1", methods=["POST"])
def receive_data1():
    global latest_data1

    data = request.get_json()
    latest_data1 = {
        "temperature": data.get("temperature"),
        "humidity": data.get("humidity"),
        "timestamp": datetime.now().isoformat()
    }

    print(latest_data1)

    return jsonify({"status": "received"}), 200


@app.route("/data1", methods=["GET"])
def send_data1():
    if latest_data1:
        return jsonify(latest_data1), 200
    else:
        return jsonify({"message": "No data yet"}), 200




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
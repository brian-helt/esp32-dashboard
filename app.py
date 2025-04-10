from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Store the latest value in memory (can switch to DB later)
latest_value = {"value": None}

@app.route("/")
def index():
    return render_template("index.html", value=latest_value["value"])

@app.route("/api/sensor-data", methods=["POST"])
def sensor_data():
    data = request.get_json()
    if "value" in data:
        latest_value["value"] = data["value"]
        print(f"Received: {data['value']}")
        return '', 204
    return 'Bad request', 400

@app.route("/api/latest", methods=["GET"])
def get_latest():
    return jsonify(latest_value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Store the latest value in memory (can switch to DB later)
latest_value = {"value": None}

def classify_lux_value(lux):
    print(type(lux))
    if lux is None:
        return "No Data"
    elif lux < 10:
        return "Nighttime"
    elif lux < 50:
        return "Very Dark"
    elif lux < 100:
        return "Dim Evening"
    elif lux < 500:
        return "Normal Indoor Lighting or Evening"
    elif lux < 1000:
        return "Bright Indoor Lighting or Overcast Day"
    elif lux < 5000:
        return "Shaded Outdoor Lighting"
    elif lux < 10000:
        return "Full Daylight, Indirect Sun"
    elif lux < 30000:
        return "Direct Sunlight"
    elif lux >= 30000:
        return "Very Bright Direct Sunlight"
        


@app.route("/")
def index():
    return render_template("index.html", value=latest_value["value"])

@app.route("/about")
def about():
    return render_template("about.html")

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
    response = {
        "value" : latest_value["value"],
        "classification" : classify_lux_value(latest_value["value"])
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
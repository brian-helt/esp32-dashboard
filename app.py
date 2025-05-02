from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Store the latest value in memory (can switch to DB later)
latest_value = {"lux": None, "temperature" : None, "humidity" : None}

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
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/api/sensor-data", methods=["POST"])
def sensor_data():
    data = request.get_json()
    if "lux" in data:
        latest_value["lux"] = data["lux"]
        print(f"Received Lux: {data['lux']}")
        return '', 204
    if "temperature" in data:
        latest_value['temperature'] = data["temperature"]
        print(f"Received Temperature: {data['temperature']}")
        return '', 204
    if "humidity" in data:
        latest_value['humidity'] = data["humidity"]
        print(f"Received Humiduty: {data['humidity']}")
        return '', 204    
    
    return 'Bad request', 400

@app.route("/api/latest", methods=["GET"])
def get_latest():
    response = {
        "lux" : latest_value["lux"],
        "classification" : classify_lux_value(latest_value["lux"]),
        "temperature" : latest_value['temperature'],
        "humidity" : latest_value['humidity']
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
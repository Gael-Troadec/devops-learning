from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Meteo app"

@app.route("/Paris")
def paris():
    return "Paris: 15°C"

@app.route("/Lyon")
def Lyon():
    return "Lyon: 18°C"

@app.route("/api/paris")
def api_paris():
    return jsonify({"ville": "Paris", "temp": 15})

if __name__ == "__main__":
    app.run(debug=True)
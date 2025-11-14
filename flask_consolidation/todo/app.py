from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def TODO_App():
    return "TODO App"

@app.route("/tasks")
def tasks():
    return "Arreter de douter de moi et mes capacites"

@app.route("/api/tasks")
def api_tasks():
    return jsonify({"task": ["Apprendre Docker", "Faire courses"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
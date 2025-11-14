from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def Omnissiah_Hall():
    return 'Welcome to the Omnissiah Sanctuary of Mars'

@app.route('/God')
def God():
    return 'You shall prey for the Machine God'

@app.route('/Hall')
def Hall():
    return "Hall of the divine figure of the Adeptus Mechanicus"

@app.route('/Machine')
def Machine():
    return "Hear the echoes of the Machine Spirit"

@app.route('/Machine/Spirit')
def get_Spirit():
    Spirit = [{'Name' : 'Silica Animus', 'Fonction' : 'Artificial Intelligence'}]
    return jsonify(Spirit)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/checkin/<projectid>/<int:qty>')
def checkIn_hardware(projectid, qty):
    return jsonify({'message': f'{qty} hardware checked in', 'projectid': projectid, 'quantity': qty})

@app.route('/api/checkout/<projectid>/<int:qty>')
def checkOut_hardware(projectid, qty):
    return jsonify({'message': f'{qty} hardware checked out', 'projectid': projectid, 'quantity': qty})

@app.route('/api/join/<projectid>')
def joinProject(projectid):
    return jsonify({'message': f'Joined {projectid}', 'projectid': projectid})

@app.route('/api/leave/<projectid>')
def leaveProject(projectid):
    return jsonify({'message': f'Left {projectid}', 'projectid': projectid})

# @app.route('/favicon.png')
# def ignore_favicon():
#     return "", 204

if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify
from time import strftime
from socket import gethostname
from socket import gethostbyname
app = Flask(__name__)
@app.route('/')
def welcome():
    message = 'Please add /docker after the port 8888'
    return message
    
@app.route('/docker')
def docker():
    currentDate = strftime('%d/%m/%y')
    currentTime = strftime('%H:%M:%S')
    currentHostname = gethostname()
    currentIPNumber = gethostbyname(gethostname())
    date = f' The current date is: {currentDate}'
    time = f' The current time is: {currentTime}'
    hostname = f' The hostname is: {currentHostname}'
    ipNumber = f' The IP number is: {currentIPNumber}'
    docker = {
        'Date' : date,
        'Time' : time,
        'Hostname' : hostname,
        'IP Number' : ipNumber
    }
    return jsonify(docker)
if __name__ == '__main__':
    app.run(debug=True , port=8888 , host='0.0.0.0')
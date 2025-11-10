from flask import Flask, jsonify
import datetime
import socket
import os

app = Flask(__name__)

@app.route('/api/v1/${{values.api_path}}')
def details():
    return jsonify({
        'message': 'Hello World from Python Flask App: ${{values.component_name}}',
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'server': socket.gethostname(),
        'env(APP_ENVIRONMENT)': os.getenv('APP_ENV', 'Not Set Yet'),
        'env(INFRA_DATA)': os.getenv('INFRA_DATA', 'Not Set Yet')
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")
from flask import Flask, request, jsonify
from swagger_parser import ENDPOINTS
import os
import json

app = Flask('swagger-mock')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'])
def index(u_path):
    key = '/' + u_path[:-1] if u_path.endswith('/') else '/' + u_path
    method = request.method
    data = {"error": "no mock found for this Endpoint or Method"}

    if key in ENDPOINTS.keys():
        if method in ENDPOINTS[key]:
            file = 'static/mocks%s[%s].json' % (key, method)
            with open(os.path.abspath(file)) as json_file:
                data = json.load(json_file)

            return jsonify(data)

    return jsonify(data)


if __name__ == '__main__':
    app.run()





from flask import Flask, abort, request
import os
import socket

app = Flask(__name__)
D = {}
@app.route('/kvs' , methods=['GET', 'DEL'])
def kvsReturn():
    if((request.args.get('value') is None)):
        if request.method == 'GET':
            if request.args.get('key') in D:
			    return D[request.args.get('key')]
            else:
                return 'error' , 404
        if request.method == 'DEL':
            if request.args.get('key') in D:
                del D[request.args.get('key')]
                return 'Success'
            else:
                return 'error' , 404
        else:
            abort(404)
@app.route('/kvs', methods=['POST','PUT'])
def kvsPosPut():
    if request.method == 'PUT' or request.method == 'POST':
        D[request.args.get('key')] = request.args.get('value')
        return 'replaced', 201
    else:
        abort(404)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for, abort
# from weather import query_api

app = Flask(__name__)

current_time = 0
username = ""
password = ""


@app.route('/login', methods=['POST'])
def login():
    if not request.json or "username" not in request.json or "password" not in request.json:
        return "Not all login info present"
    username = request.json['username']
    password = request.json['password']
    return "This request is valid, needs to be implemented"
    # send auth_request to database


@app.route('/relogin', methods=['GET'])
def relogin():
    # send auth_request to database
    return "This method will reauthenticate the user with stored credentials"


@app.route('/get_data', methods=['GET'])
def index():
    return "This web page is working.... -Eric"


@app.route('/update_data', methods=['PUT'])
def put_method():
    print(request.json)
    if not request.json or "login_key" not in request.json or "row_key" not in request.json or "glucometer_data" not in request.json:
        abort(400)
    # make database call here

    #act based upon database return
    if 'login_key' in request.json:
        return 'Success'
    else:
        return 'Failure'


@app.route('/new_data', methods=['POST'])
def post_method():
    return "This post requires an input of login key, new information"


@app.route('/delete/<login_key>/<row_key>', methods=['DELETE'])
def delete_entry():
    #make database call here
    return "This delete method deletes a new entry based on login key, row key"


if __name__=='__main__':
   app.run(debug=True)

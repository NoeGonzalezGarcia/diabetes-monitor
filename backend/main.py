#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for, abort
from flask_cors import CORS
import dbWrapper
import dateparser

app = Flask(__name__)
CORS(app)
wrapper = dbWrapper("admin", "admin")
wrapper.add_patient("I live horribly", 1, "admin", "1234", "Joe", "R", "Smith")


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return "working"


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


@app.route('/get_data/<', methods=['GET'])
def index():
    print("placeholder")


@app.route('/update_data', methods=['PUT'])
def put_method():
    print(request.json)
    if not request.json or "login_key" not in request.json or "row_key" not in request.json or "glucometer_data" not in request.json:
        abort(400)
    # make database call here
    # act based upon database return
    if 'login_key' in request.json:
        return 'Success'
    else:
        return 'Failure'


@app.route('/new_data', methods=['PUT'])
def post_method():
    if not request.json:
        abort(404)
    breakfast = request.json[1]
    lunch = request.json[2]
    dinner = request.json[3]
    meals = {breakfast, lunch, dinner}
    for i in meals:
        current_object = i
        if i['calories'] != "null":
            date = parse_date(current_object['date'])
            wrapper.add_smbg_data("admin", date[1], date[2],
                                  date[3], current_object['meal_type'],
                                  current_object['blood_sugar']['pre'],
                                  current_object['blood_sugar']['post'], current_object['calories'])
    return "success"


@app.route('/delete/<login_key>/<row_key>', methods=['DELETE'])
def delete_entry():
    # make database call here
    return "This delete method deletes a new entry based on login key, row key"


def parse_date(date):
    parsed_date = str(dateparser.parse(date)).split(" ")
    parsed_date = parsed_date[0].split("-")
    return parsed_date[1], parsed_date[2], parsed_date[0]


if __name__=='__main__':
   app.run(debug=True)



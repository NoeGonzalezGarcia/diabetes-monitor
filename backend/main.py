#!/usr/bin/env python

import dateparser
from flask import Flask, request, abort
from flask_cors import CORS
import encryption
import dbWrapper

username = "admin2"

app = Flask(__name__)
CORS(app)
wrapper = dbWrapper.dbWrapper("root", "root33")
wrapper.add_patient(5, "I live wonderfully", 1, username, "1234", "Joe", "R", "Smith")
e, keyCombo = encryption.generateKeys()
pub, pri = keyCombo


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


@app.route('/get_data/<date>/<meal>', methods=['GET'])
def get_user_date_meal(date, meal):
    date_parsed = parse_date(date)
    print(date)
    print(meal)
    if date != "" and (meal == "Breakfast" or meal == "Lunch" or meal == "Dinner"):
        print(wrapper.get_smbg_data(username, date_parsed, meal, pri, e))
        return wrapper.get_smbg_data(username, date_parsed, meal, pri, e)
    return ""


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
    print(request.json)
    breakfast = request.json['body'][0]
    lunch = request.json['body'][1]
    dinner = request.json['body'][2]
    meals = list()
    meals.append(breakfast)
    meals.append(lunch)
    meals.append(dinner)
    for i in meals:
        current_object = i
        if i['Calories'] != "":
            date = parse_date(current_object['Date'])
            wrapper.add_smbg_data("admin2", date, encryption.encrypt(pub, e, current_object['Mealtype']),
                                  encryption.encrypt(pub, e, current_object['BloodSugar']['pre']),
                                  encryption.encrypt(pub, e, current_object['BloodSugar']['post']), encryption.encrypt(pub, e, current_object['Calories']))
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
   app.run(debug=False)



import MySQLdb
import datetime
import json
from .encryption import *


class dbWrapper:
    def __init__(self, user, password):
        self.__db = MySQLdb.connect(
            "localhost",    # host name
            user,           # username of db
            password)       # password of db
        self.__cur = self.__db.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS diabetes_monitor"
        self.__cur.execute(sql)
        sql = "USE diabetes_monitor"
        self.__cur.execute(sql)
        sql = "SET autocommit=1;"
        self.__cur.execute(sql)
        self.__create_user_info_table()
        self.__create_patient_table()
        self.__create_meals_table()
        self.__create_smbg_data_table()
        self.__create_user_lookup_table()

    # Creates the user_info table if it doesn't exist already
    def __create_user_info_table(self):
        sql = "CREATE TABLE IF NOT EXISTS user_info (" \
              "id INTEGER UNSIGNED NOT NULL," \
              "password VARCHAR(255) NOT NULL," \
              "first_name VARCHAR(80) NOT NULL," \
              "middle_initial VARCHAR(20)," \
              "last_name VARCHAR(80) NOT NULL," \
              "PRIMARY KEY (id) )"
        self.__cur.execute(sql)

    # Creates the patient table if it doesn't exist already
    def __create_patient_table(self):
        sql = "CREATE TABLE IF NOT EXISTS patient (" \
              "id INTEGER UNSIGNED NOT NULL," \
              "lifestyle_info VARCHAR(10000)," \
              "diabetes_type INTEGER UNSIGNED NOT NULL," \
              "FOREIGN KEY (id) REFERENCES user_info(id) )"
        self.__cur.execute(sql)

    # Creates the SMBG data table if it doesn't exist already
    def __create_smbg_data_table(self):
        sql = "CREATE TABLE IF NOT EXISTS smbg_data (" \
              "user_date_meal VARCHAR(80) NOT NULL," \
              "id INTEGER UNSIGNED NOT NULL," \
              "meal_id INTEGER UNSIGNED NOT NULL," \
              "date DATE NOT NULL," \
              "pre_meal_smbg_level INTEGER UNSIGNED NOT NULL," \
              "post_meal_smbg_level INTEGER UNSIGNED NOT NULL," \
              "caloric_intake INTEGER UNSIGNED NOT NULL," \
              "PRIMARY KEY (user_date_meal)," \
              "FOREIGN KEY (id) REFERENCES user_info(id)," \
              "FOREIGN KEY (meal_id) REFERENCES meals(meal_id) )"
        self.__cur.execute(sql)

    # Creates the meals table if it doesn't exist already. Includes Breakfast, Lunch, and Dinner.
    def __create_meals_table(self):
        table_exists = True
        try:
            sql = "SELECT 1 FROM meals LIMIT 1;"
            self.__cur.execute(sql)
        except: # meals table doesn't exist
            table_exists = False
        if not table_exists:
            sql = "CREATE TABLE IF NOT EXISTS meals (" \
                  "meal_id INTEGER UNSIGNED NOT NULL," \
                  "meal_name VARCHAR(20) NOT NULL," \
                  "PRIMARY KEY (meal_id) )"
            self.__cur.execute(sql)
            meals = ["breakfast", "lunch", "dinner"]
            for i, meal in enumerate(meals):
                sql = "INSERT INTO meals (meal_id, meal_name)" \
                      "VALUES("+str(i)+", '"+meal+"');"
                self.__cur.execute(sql)

    # Creates the user_lookup table if it doesn't exist already.
    # Used to get the id of a particular user with their username.
    def __create_user_lookup_table(self):
        sql = "CREATE TABLE IF NOT EXISTS user_lookup (" \
              "username VARCHAR(80) NOT NULL," \
              "id INTEGER UNSIGNED NOT NULL," \
              "PRIMARY KEY(username)," \
              "FOREIGN KEY (id) REFERENCES user_info(id) )"
        self.__cur.execute(sql)

    # Adds a new patient to the database. Users id's are auto-incremented.
    # User id is made the same in user_info, patient, and user_lookup tables.
    def add_patient(self, patient_id, lifestyle_info, diabetes_type, username, password,
                    first_name, middle_initial, last_name):
        sql = "SELECT * FROM user_info WHERE id = "+str(patient_id)+";"
        self.__cur.execute(sql)
        result = self.__cur.fetchall()
        if len(result) == 0:
            sql = "INSERT INTO user_info (id, password, first_name, middle_initial, last_name) " \
                  "VALUES (" + str(patient_id) + ", '" + password + "', '" + first_name + "', '" \
                  + middle_initial + "', '" + last_name + "');"
            self.__cur.execute(sql)
            sql = "INSERT INTO user_lookup (username, id) " \
                  "VALUES('" + username + "', " + str(patient_id) + ");"
            self.__cur.execute(sql)
            sql = "INSERT INTO patient (id, lifestyle_info, diabetes_type)" \
                  "VALUES('" + str(patient_id) + "', '" + lifestyle_info + "', '" + str(diabetes_type) + "');"
            self.__cur.execute(sql)

    # # Gets the current id that is auto-incremented in user_info table.
    # def __get_user_info_current_index(self):
    #     sql = "SELECT 'AUTO_INCREMENT' FROM INFORMATION_SCHEMA.TABLES " \
    #           "WHERE TABLE_SCHEMA = 'diabetes_monitor' AND TABLE_NAME = 'user_info';"
    #     self.__cur.execute(sql)
    #     result = self.__cur.fetchone()
    #     print(result)
    #     return result[0]

    # Gets the id of a user from their username.
    def __lookup_patient_id(self, username):
        sql = "SELECT id FROM user_lookup WHERE username = '"+username+"';"
        self.__cur.execute(sql)
        result = self.__cur.fetchone()
        a,b = result + (0, )
        # print(a)
        return result[0]

    def get_patient_info(self, username):
        id = self.__lookup_patient_id(username)
        # TODO: implement me

    # Adds an smbg data entry into the smbg_data table, specific to a user's username and a date.
    # Has a meal which is either Breakfast, Lunch, or Dinner.
    def add_smbg_data(self, username, date, meal, pre_meal_smbg, post_meal_smbg, caloric_intake):
        id = self.__lookup_patient_id(username)
        meal_id = self.__get_meal_index(meal)
        date_formatted = date[2] + "-" + date[0] + "-" + date[1]
        key = "'"+str(id)+"-"+date_formatted+"-"+str(meal_id)+"'"
        sql = "SELECT * FROM smbg_data WHERE user_date_meal = "+key+";"
        self.__cur.execute(sql)
        result = self.__cur.fetchall()
        if len(result) == 0:
            sql = "INSERT INTO smbg_data (user_date_meal, id, meal_id, date, " \
                  "pre_meal_smbg_level, post_meal_smbg_level, caloric_intake)" \
                  "VALUES("+key+", "+str(id)+", "+str(meal_id)+", '"+date_formatted+"', " + \
                  str(pre_meal_smbg)+", "+str(post_meal_smbg)+", "+str(caloric_intake)+");"
            # print(sql)
            self.__cur.execute(sql)

    # Returns a formatted date string with a given day, month, year.
    def __make_date(self, day, month, year):
        date = datetime.date(year, month, day)
        return date.strftime('%Y-%m-%d')

    # Returns the meal index of the specified meal.
    def __get_meal_index(self, meal_name):
        sql = "SELECT meal_id FROM meals WHERE meal_name = '"+meal_name+"';"
        self.__cur.execute(sql)
        result = self.__cur.fetchone()
        a,b = result + (0, )
        return result[0]

    # Returns SMBG data as JSON for a particular username, on a particular date and meal_name
    def get_smbg_data(self, username, date, meal_name, pri, e):
        id = self.__lookup_patient_id(username)
        meal_id = self.__get_meal_index(meal_name)
        return self.__get_meal_data(id, date, meal_id, pri, e)

    # Returns SMBG data as JSON given a user id, date, and meal id
    def __get_meal_data(self, user_id, date, meal_id, pri, e):
        date_formatted = date[2] + "-" + date[0] + "-" + date[1]
        key = "'" + str(user_id) + "-" + date_formatted + "-" + str(meal_id) + "'"
        sql = "SELECT user_date_meal, pre_meal_smbg_level, post_meal_smbg_level, caloric_intake FROM smbg_data" \
              " WHERE user_date_meal = "+key+";"
        #print(sql)
        self.__cur.execute(sql)
        row = self.__cur.fetchone()
        #print(row)
        pre_meal_smbg = row[1]
        post_meal_smbg = row[2]
        caloric_intake = row[3]
        return self.__create_meal_json_object(pre_meal_smbg, post_meal_smbg, caloric_intake, pri, e)

    # Creates a JSON of for a meal's SMBG data.
    def __create_meal_json_object(self, pre_meal_smbg, post_meal_smbg, caloric_intake, pri, e):
        data = {}
        data['pre_meal_smbg'] = decrypt(pri, e, pre_meal_smbg)
        data['post_meal_smbg'] = decrypt(pri, e, post_meal_smbg)
        data['caloric_intake'] = decrypt(pri, e, caloric_intake)
        return json.dumps(data)

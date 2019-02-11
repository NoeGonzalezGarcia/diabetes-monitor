import MySQLdb
import datetime


class dbWrapper:
    def __init__(self, user, password):
        self.__db = MySQLdb.connect(
            "localhost",    # host name
            user,           # username of db
            password)       # password of db
        self.__cur = self.__db.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS diabetes_monitor"
        self.__cur.execute(sql)
        self.__create_user_info_table()
        self.__create_patient_table()
        self.__create_smbg_data_table()
        self.__create_meals_table()
        sql = "USE diabetes_monitor"
        self.__cur.execute(sql)

    # Creates the user_info table if it doesn't exist already
    def __create_user_info_table(self):
        sql = "CREATE TABLE IF NOT EXISTS user_info (" \
              "id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT," \
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
              "FOREIGN KEY (id) )"
        self.__cur.execute(sql)

    # Creates the SMBG data table if it doesn't exist already
    def __create_smbg_data_table(self):
        sql = "CREATE TABLE IF NOT EXISTS smbg_data (" \
              "date DATE NOT NULL," \
              "id INTEGER UNSIGNED NOT NULL," \
              "meal-id INTEGER UNSIGNED NOT NULL," \
              "pre_meal_smbg_level INTEGER UNSIGNED NOT NULL," \
              "post_meal_smbg_level INTEGER UNSIGNED NOT NULL," \
              "caloric_intake INTEGER UNSIGNED NOT NULL," \
              "PRIVATE KEY(date)," \
              "FOREIGN KEY(id)," \
              "FOREIGN KEY(meal_id) );"
        self.__cur.execute(sql)

    # Creates the meals table if it doesn't exist already. Includes Breakfast, Lunch, and Dinner.
    def __create_meals_table(self):
        sql = "CREATE TABLE IF NOT EXISTS meals (" \
              "meal_id INTEGER UNSIGNED NOT NULL," \
              "meal_name VARCHAR(20) NOT NULL," \
              "PRIVATE KEY(meal_id) );"
        self.__cur.execute(sql)
        meals = ["Breakfast", "Lunch", "Dinner"]
        for i, meal in meals:
            sql = "INSERT INTO meals (meal_id, meal_name)" \
                  "VALUES("+i+", "+meal+");"
            self.__cur.execute(sql)

    # Creates the user_lookup table if it doesn't exist already.
    # Used to get the id of a particular user with their username.
    def __create_user_lookup_table(self):
        sql = "CREATE TABLE IF NOT EXISTS user_lookup (" \
              "username VARCHAR(80) NOT NULL," \
              "id INTEGER UNSIGNED NOT NULL," \
              "PRIVATE KEY(username)," \
              "FOREIGN KEY(id) );"
        self.__cur.execute(sql)

    # Adds a new patient to the database. Users id's are auto-incremented.
    # User id is made the same in user_info, patient, and user_lookup tables.
    def add_patient(self, lifestyle_info, diabetes_type, username, password,
                    first_name, middle_initial, last_name):
        sql = "INSERT INTO user_info (password, first_name, middle_initial, last_name)" \
              "VALUES("+password+", "+first_name+", "+middle_initial+", "+last_name+");"
        self.__cur.execute(sql)
        cur_user_index = self.__get_user_info_current_index()
        sql = "INSERT INTO patient (id, lifestyle_info, diabetes_type)" \
              "VALUES("+cur_user_index+", "+lifestyle_info+", "+diabetes_type+");"
        self.__cur.execute(sql)
        sql = "INSERT INTO user_lookup (username, id) " \
              "VALUES("+username+", "+cur_user_index+");"
        self.__cur.execute(sql)

    # Gets the current id that is auto-incremented in user_info table.
    def __get_user_info_current_index(self):
        sql = "SELECT 'AUTO_INCREMENT' FROM INFORMATION_SCHEMA.TABLES" \
              "WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'user_info';"
        self.__cur.execute(sql)
        return self.__cur.fetchone()

    # Gets the id of a user from their username.
    def __lookup_patient_id(self, username):
        sql = "SELECT id FROM user_lookup WHERE username = '"+username+"';"
        self.__cur.execute(sql)
        return self.__cur.fetchone()

    # Adds an smbg data entry into the smbg_data table, specific to a user's username and a date.
    # Has a meal which is either Breakfast, Lunch, or Dinner.
    def add_smbg_data(self, username, day, month, year, meal, pre_meal_smbg, post_meal_smbg, caloric_intake):
        id = self.__lookup_patient_id(username)
        date = self.__make_date(day, month, year)
        meal_id = self.__get_meal_index(meal)
        sql = "INSERT INTO smbg_data (date, id, meal_id, pre_meal_smbg_level, post_meal_smbg_level, caloric_intake)" \
              "VALUES("+date+", "+id+", "+meal_id+", "+pre_meal_smbg+", "+post_meal_smbg+", "+caloric_intake+");"
        self.__cur.execute(sql)

    # Returns a formatted date string with a given day, month, year.
    def __make_date(self, day, month, year):
        date = datetime.date(year, month, day)
        return date.strftime('%Y-%m-%d')

    # Returns the meal index of the specified meal.
    def __get_meal_index(self, meal):
        sql = "SELECT meal_id FROM meals WHERE meal_name = '"+meal+"';"
        self.__cur.execute(sql)
        return self.__cur.fetchone()

    def get_smbg_data(self, username, day, month, year):
        return "placeholder"

import MySQLdb


class dbWrapper:
    def __init__(self, user, password):
        self.db = MySQLdb.connect(
            "localhost",    # host name
            user,           # username of db
            password)       # password of db
        self.cur = self.db.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS diabetes_monitor"
        self.cur.execute(sql)
        self.create_user_info_table()
        self.create_patient_table()
        self.create_smbg_data_table()
        self.create_meals_table()
        sql = "USE diabetes_monitor"
        self.cur.execute(sql)

        # TODO: create user lookup table that gets an id with username?

    def create_user_info_table(self):
        sql = "CREATE TABLE IF NOT EXISTS user_info (" \
              "id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT," \
              "password VARCHAR(255) NOT NULL," \
              "first_name VARCHAR(80) NOT NULL," \
              "middle_initial VARCHAR(20)," \
              "last_name VARCHAR(80) NOT NULL," \
              "PRIMARY KEY (id) )"
        self.cur.execute(sql)

    def create_patient_table(self):
        sql = "CREATE TABLE IF NOT EXISTS patient (" \
              "id INTEGER UNSIGNED NOT NULL," \
              "lifestyle_info VARCHAR(10000)," \
              "diabetes_type INTEGER UNSIGNED NOT NULL," \
              "FOREIGN KEY (id) )"
        self.cur.execute(sql)

    def create_smbg_data_table(self):
        sql = "CREATE TABLE IF NOT EXISTS smbg_data (" \
              "date DATE NOT NULL," \
              "meal-id INTEGER UNSIGNED NOT NULL," \
              "pre_meal_smbg_level INTEGER UNSIGNED NOT NULL," \
              "post_meal_smbg_level INTEGER UNSIGNED NOT NULL," \
              "caloric_intake INTEGER UNSIGNED NOT NULL," \
              "PRIVATE KEY(date)," \
              "FOREIGN KEY(meal_id) );"
        self.cur.execute(sql)

    def create_meals_table(self):
        sql = "CREATE TABLE IF NOT EXISTS meals (" \
              "meal_id INTEGER UNSIGNED NOT NULL," \
              "meal_name VARCHAR(20) NOT NULL," \
              "PRIVATE KEY(meal_id) );"
        self.cur.execute(sql)
        meals = ["Breakfast", "Lunch", "Dinner"]
        for i, meal in meals:
            sql = "INSERT INTO meals (meal_id, meal_name) VALUES" \
                  "("+i+", "+meal+"));"
            self.cur.execute(sql)

    def create_user_lookup_table(self):
        sql = "CREATE TABLE IF NOT EXISTS user_lookup (" \
              "username VARCHAR(80) NOT NULL," \
              "id INTEGER UNSIGNED NOT NULL," \
              "PRIVATE KEY(username)," \
              "FOREIGN KEY(id) );"
        self.cur.execute(sql)

    def add_patient(self, lifestyle_info, diabetes_type, username, password,
                    first_name, middle_initial, last_name):
        sql = "INSERT INTO user_info (password, first_name, middle_initial, last_name) VALUES" \
              "("+password+", "+first_name+", "+middle_initial+", "+last_name+"));"
        self.cur.execute(sql)
        cur_user_index = self.get_user_info_current_index()
        sql = "INSERT INTO patient (id, lifestyle_info, diabetes_type) VALUES" \
              "("+cur_user_index+", "+lifestyle_info+", "+diabetes_type+"));"
        self.cur.execute(sql)
        sql = "INSERT INTO user_lookup (username, id) VALUES" \
              "("+username+", "+cur_user_index+"));"
        self.cur.execute(sql)

    def get_user_info_current_index(self):
        sql = "SELECT 'AUTO_INCREMENT' FROM INFORMATION_SCHEMA.TABLES" \
              "WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'user_info';"
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_patient(self, username):  # TODO: How to get a user? - username?



    def search_patient(self):   # Do we need this?


    def add_smbg_data(self, username, date, meal, pre_meal_smbg, post_meal_smbg, caloric_intake):
        sql = "INSERT INTO "

    def get_smbg_data(self, username, date):


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

    def create_user_info_table(self, cur):
        sql = "CREATE TABLE IF NOT EXISTS USER_INFO (" \
              "id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT," \
              "username VARCHAR(80) NOT NULL," \
              "password VARCHAR(255) NOT NULL," \
              "first_name VARCHAR(80) NOT NULL," \
              "middle_initial VARCHAR(20)" \
              "last_name VARCHAR(80) NOT NULL," \
              "PRIMARY KEY (id) )"
        cur.execute(sql)

    def create_patient_table(self, cur):
        sql = "CREATE TABLE IF NOT EXISTS PATIENT (" \
              "id INTEGER UNSIGNED NOT NULL" \
              "lifestyle_info VARCHAR(10000)," \
              "diabetes_type INTEGER UNSIGNED NOT NULL," \
              "FOREIGN KEY (id) )"
        cur.execute(sql)
# @Author: simon
# @Date:   2020-03-18T18:02:49+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-21T08:51:25+01:00

import pymysql as sql

from app import app

class DataBase:

    def __init__(self):
        if not hasattr(self, 'database'):
            self.connect();

    def query(self, request, parameters = [], get_result = False):
        if (not hasattr(self, 'database')) or (self.database == None):
            print("DataBase query error : Database not connected")
            return None;
        try:
            with self.database.cursor() as cursor:
                nb = cursor.execute(request, parameters)
                if get_result == True:
                    result = cursor.fetchall()
            if not get_result:
                self.database.commit()
                if nb != 0:
                    return True
                else:
                    return False
            else:
                return result
        except Exception:
            self.disconnect()
            return None

    def connect(self):
        try:
            self.database = sql.connect(
                host        = app.config["DATABASE_HOST"],
                unix_socket = app.config["DATABASE_SOCK"],
                user        = app.config["DATABASE_USER"],
                passwd      = app.config["DATABASE_PASS"],
                db          = app.config["DATABASE_NAME"],
                cursorclass = sql.cursors.DictCursor)
            print("Database: Connected")
        except Exception as e:
            print("DataBase connection exception : ", e)
            print("Fatal error: database connection")
            self.database = None

    def disconnect(self):
        if (not hasattr(self, 'database')) or (self.database == None):
            return False;
        self.database.close()
        return True

    def get_last_insert_id(self):
        return self.database.insert_id()

    def __del__(self):
        self.disconnect()
        print("Database: Disconnected")

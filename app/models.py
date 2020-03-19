# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-19T18:59:11+01:00

from .DataBase import DataBase

class User_modele:

    def __init__(self):
        self.db = DataBase()

    def user_exist(self, username, password = None):
        parameters = [username]
        if not password is None:
            query = "SELECT user_id FROM user WHERE username=%s AND password=%s"
            parameters.append(password)
        else:
            query = "SELECT user_id FROM user WHERE username=%s"
        result = self.db.query(query, parameters, True)
        if len(result) == 0:
            return False
        return True

    def get_info(self, username):
        query = "SELECT user_id, username, password, logged FROM user WHERE username=%s"
        result = self.db.query(query, [username], True)
        if len(result) == 0:
            return None
        return result[0]

    def signin(self, username, password):
        if not self.user_exist(username, password):
            return False
        query = "UPDATE user SET logged=True WHERE username=%s"
        self.db.query(query, [username], False)
        return True

    def signout(self, username):
        if not self.user_exist(username):
            print("user modele : signout : user doesn't exist")
            return False
        query = "UPDATE user SET logged=False WHERE username=%s"
        self.db.query(query, [username], False)
        return True

    def register(self, username, password):
        query = "INSERT INTO user(username, password) VALUES (%s, %s)"
        self.db.query(query, [username, password], False)
        return True

class Task_modele:

    def __init__(self):
        pass

    def get_task_all(self):
        pass

    def get_task_id(self, id):
        pass

    def upd_task_id(self, id):
        pass

    def set_task(self):
        pass

    def del_task_id(self, id):
        pass

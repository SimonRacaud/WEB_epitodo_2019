# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-18T19:14:05+01:00

from .DataBase import DataBase

class User_modele:

    def __init__(self):
        self.db = DataBase()

    def get_info(self):
        query = "SELECT user_id, username, password, logged FROM user WHERE username=%s"
        result = self.db.query(query, ["simon"], True)
        return result[0]

    def signin(self):
        pass

    def signout(self):
        pass

    def register(self):
        pass

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

# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-19T16:48:51+01:00

from flask import render_template
from flask import jsonify

from app import models
from .models import User_modele
from .models import Task_modele
from .app_session import AppSession

class Task_controller:

    def __init__(self):
        self.task_modele = Task_modele()
        self.session = AppSession()

    def get_all(self):
        pass

    def get_with_id(self):
        pass

    def set_with_id(self):
        pass

    def set_new(self):
        pass

    def del_with_id(self):
        pass

class User_controller:

    def __init__(self):
        self.usr_modele = User_modele()

    def get_information(self):
        data = self.usr_modele.get_info()
        data["key1"] = data.pop("username")
        data["key2"] = data.pop("password")
        return jsonify(result = data);

    def signin(self, username, password):
        if self.session.is_logged():
            return "User already logged"
        else:
            self.session.set_session(username)
            return "OK"

    def signout(self):
        if self.session.is_logged():
            self.session.del_session()
            return "OK"
        else:
            return "User not logged"

    def register(self, username, password):
        return "Register"


class AppController(Task_controller, User_controller):

    def __init__(self):
        Task_controller.__init__(self)
        User_controller.__init__(self)

    def get_home_page(self):
        return render_template("index.html", title="MAIN PAGE")

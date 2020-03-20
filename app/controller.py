# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-20T12:31:32+01:00

from flask import render_template
from flask import jsonify
from flask import session
from flask import json

import os

from app import app
from app import models
from .models import User_modele
from .models import Task_modele
from .app_session import AppSession

class Task_controller:

    def __init__(self):
        self.task_modele = Task_modele()

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
        if self.is_logged():
            username = self.session.get_username()
            data = self.usr_modele.get_info(username)
            data["key1"] = data.pop("username")
            data["key2"] = data.pop("password")
            return jsonify(result = data);
        else:
            return self.get_json_file_content("INTERNAL_ERR.json")

    def signin(self, username, password):
        if self.is_logged():
            return self.get_json_file_content("INTERNAL_ERR.json")
        else:
            if self.usr_modele.signin(username, password):
                if self.session.set_session(username):
                    return self.get_json_file_content("SIGNIN_RES.json")
                else:
                    return self.get_json_file_content("INTERNAL_ERR.json")
            else:
                return self.get_json_file_content("SIGNIN_ERR.json")

    def signout(self):
        if self.is_logged():
            username = self.session.get_username()
            self.session.del_session()
            self.usr_modele.signout(username)
            return self.get_json_file_content("SIGNOUT_RES.json")
        else:
            return self.get_json_file_content("INTERNAL_ERR.json")

    def register(self, username, password):
        if self.is_logged():
            return self.get_json_file_content("INTERNAL_ERR.json")
        else:
            if self.usr_modele.register(username, password):
                return self.get_json_file_content("REGISTER_RES.json")
            else:
                return self.get_json_file_content("REGISTER_ERR_EXIST.json")

class AppController(Task_controller, User_controller):

    def __init__(self):
        self.session = AppSession()
        Task_controller.__init__(self)
        User_controller.__init__(self)

    def get_json_file_content(self, filename):
            filepath = os.path.join(app.static_folder, "json", filename)
            try:
                with open(filepath, "r") as file:
                    data = json.load(file)
                return data
            except FileNotFoundError:
                return jsonify(error = "internal error")

    def is_logged(self):
        if not self.session.exist():
            print("is_logged : Session doesn't exist")
            return False
        username = self.session.get_username()
        userinfo = self.usr_modele.get_info(username)
        if (not userinfo is None) and (userinfo["logged"] == True):
            return True
        else:
            print("is_logged: User not logged in database")
        return False

    def get_home_page(self):
        return render_template("index.html", title="MAIN PAGE")

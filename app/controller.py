# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-18T19:23:52+01:00

from flask import render_template
from flask import jsonify

from app import models
from .models import User_modele

class Task_controller:

    def __init__(self):
        self.modele = Task_modele()

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
        self.session = Session(self.usr_modele)

    def get_information(self):
        data = self.usr_modele.get_info()
        #data["key1"] = data.pop("user_id")
        #data["key2"] = data.pop("username")
        #data["key3"] = data.pop("password")
        #data["key4"] = data.pop("logged")
        return jsonify(result = data);

class Session:

    def __init__(self, modele):
        self.usr_modele = modele

    def is_logged(self):
        pass

    def login(self):
        pass

    def logout(self):
        pass

    def register(self):
        pass

# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-24T11:30:45+01:00

from flask import render_template
from flask import jsonify
from flask import json

from app import app

class UserController:

    def __init__(self):
        raise Exception("Error: class not instanciable")

    def get_information(self):
        if self.is_logged():
            username = self.session.get_username()
            data = self.modele.get_info(username)
            if data == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            return jsonify(result = data);
        else:
            return self.get_json_file_content("LOGGED_ERR.json")

    def signin(self, username, password):
        if self.is_logged():
            return self.get_json_file_content("INTERNAL_ERR.json")
        else:
            ret = self.modele.signin(username, password)
            if ret == True:
                if self.session.set_session(username):
                    return self.get_json_file_content("SIGNIN_RES.json")
                else:
                    return self.get_json_file_content("INTERNAL_ERR.json")
            elif ret == False:
                return self.get_json_file_content("SIGNIN_ERR.json")
            else:
                return self.get_json_file_content("INTERNAL_ERR.json")

    def signout(self):
        if self.is_logged():
            username = self.session.get_username()
            self.session.del_session()
            ret = self.modele.signout(username)
            if ret == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            return self.get_json_file_content("SIGNOUT_RES.json")
        else:
            return self.get_json_file_content("LOGGED_ERR.json")

    def register(self, username, password):
        if self.is_logged():
            return self.get_json_file_content("INTERNAL_ERR.json")
        else:
            ret = self.modele.register(username, password)
            if ret == True:
                return self.get_json_file_content("REGISTER_RES.json")
            elif ret == False:
                return self.get_json_file_content("REGISTER_ERR_EXIST.json")
            else:
                return self.get_json_file_content("INTERNAL_ERR.json")

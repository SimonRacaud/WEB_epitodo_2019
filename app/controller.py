# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-20T17:53:41+01:00

from flask import render_template
from flask import jsonify
from flask import json
import os

from app import app

from .app_session import AppSession
from .models import AppModele

from .TaskController import TaskController
from .UserController import UserController

def is_id_in_tasks_id(id, array):
    for task_id in array:
        if int(id) == int(task_id['fk_task_id']):
            return True
    return False

class AppController(TaskController, UserController):
    """
        AppController class:

        #
        # Generate the views and return them
        #

        - UserController : function that manage all about users
        - TaskController : function that manage all about tasks of the users
    """
    def __init__(self):
        self.session = AppSession()
        self.modele = AppModele()

    def get_json_file_content(self, filename):
            filepath = os.path.join(app.static_folder, "json", filename)
            try:
                with open(filepath, "r") as file:
                    data = json.load(file)
                return data
            except FileNotFoundError:
                print("AppController:get_json_file_content : file not found")
                return jsonify(error = "internal error")

    def is_logged(self):
        if not self.session.exist():
            return False
        username = self.session.get_username()
        userinfo = self.modele.get_info(username)
        if userinfo == None:
            return False
        elif (not userinfo is None) and (userinfo["logged"] == True):
            return True
        else:
            print("In AppController:is_loggged()")
            print("ERROR : User not logged in database but the session exist")
        return False

    def get_home_page(self):
        return render_template("index.html", title="MAIN PAGE")

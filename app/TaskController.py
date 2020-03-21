# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-21T09:56:33+01:00

from flask import render_template
from flask import jsonify
from flask import json

from app import app

class TaskController:

    def __init__(self):
        raise Exception("Error: class not instanciable")

    def task_get_all(self):
        if self.is_logged():
            username = self.session.get_username()
            tasks = self.modele.get_task_all(username)
            if tasks == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            list_task = list()
            for task in tasks:
                element = dict()
                element["title"] = task["title"]
                element["begin"] = str(task["begin"])
                element["end"] = str(task["end"])
                element["status"] = task["status"]
                json_task = dict()
                json_task[task["task_id"]] = element
                list_task.append(json_task)
            res = dict()
            res["tasks"] = list_task
            return jsonify(result = res)
        else:
            return self.get_json_file_content("INTERNAL_ERR.json")

    def task_get_with_id(self, id):
        # (don't forget) : check if [id] is a number

        # It's just test code => to test the modele function
        username = self.session.get_username() # DEBUG
        task = self.modele.get_task_id(username, id) # DEBUG
        # ret is an dictionnary : like => task["title"]
        return jsonify(task)

    def task_update_with_id(self, id, argv):
        return "Update task"

    def task_set_new(self, argv):
        return "Add new task"

    def task_del_with_id(self, id):
        return "Remove task"

# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-20T17:23:54+01:00

from flask import render_template
from flask import jsonify
from flask import json

from app import app

class TaskController:

    def __init__(self):
        raise Exception("Error: class not instanciable")

    def get_all_task(self):
        if self.is_logged():
            username = self.session.get_username()
            tasks = self.modele.get_task_all(username)
            if tasks == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            list_task = list()
            for task in tasks:
                element = dict()
                element["title"] = task[0]["title"]
                element["begin"] = task[0]["begin"]
                element["end"] = task[0]["end"]
                element["status"] = task[0]["status"]
                json_task = dict()
                json_task[task[0]["task_id"]] = element
                list_task.append(json_task)
            res = dict()
            res["tasks"] = list_task
            return jsonify(result = res)
        else:
            return self.get_json_file_content("INTERNAL_ERR.json")

    def get_with_id(self):
        pass

    def up_with_id(self):
        pass

    def set_new(self):
        pass

    def del_with_id(self):
        pass

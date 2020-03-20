# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-20T14:14:21+01:00

from flask import render_template
from flask import jsonify
from flask import json

from app import app

class TaskController:

    def __init__(self):
        raise Exception("Error: class not instanciable")

    def get_all(self):
        if self.is_logged():
            username = self.session.get_username()
            tasks = self.modele.get_task_all(username)
            if tasks == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            list_task = list()
            for task in tasks:
                element = jsonify(title = task["title"],
                                  begin = task["begin"],
                                  end = task["end"],
                                  status = task["status"])
                json_task = jsonify(tasks["task_id"] = element)
                list_task.append(json_task)
            result = jsonify(tasks = list_task)
            return jsonify(result = result)
        else:
            return self.get_json_file_content("INTERNAL_ERR.json")

    def get_with_id(self):


    def set_with_id(self):
        pass

    def set_new(self):
        pass

    def del_with_id(self):
        pass

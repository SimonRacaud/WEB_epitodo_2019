# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-21T15:20:13+01:00

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
            return self.get_json_file_content("LOGGED_ERR.json")

    def task_get_with_id(self, id):
        if self.is_logged():
            try:
                id = int(id)
            except ValueError:
                return self.get_json_file_content("INTERNAL_ERR.json")
            username = self.session.get_username()
            task = self.modele.get_task_id(username, id);
            if task == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            ret = dict()
            ret["title"] = task["title"]
            ret["begin"] = str(task["begin"])
            ret["end"] = str(task["end"])
            ret["status"] = task["status"]
            return jsonify(result = ret)
        else:
            return self.get_json_file_content("LOGGED_ERR.json")

    def task_update_with_id(self, id, argv):
        if self.is_logged():
            try:
                id = int(id)
            except ValueError:
                return self.get_json_file_content("INTERNAL_ERR.json")
            username = self.session.get_username()
            task_update = self.modele.upd_task_id(username, id, argv);
            if task_update == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            return self.get_json_file_content("TASK_ID_MOD_RES.json")
        else:
            return self.get_json_file_content("LOGGED_ERR.json")

    def task_set_new(self, argv):
        if self.is_logged():
            username = self.session.get_username()
            task_add = self.modele.set_task(username, argv);
            if task_add == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            return self.get_json_file_content("TASK_ID_ADD_RES.json")
        else:
            return self.get_json_file_content("LOGGED_ERR.json")

    def task_del_with_id(self, id):
         if self.is_logged():
             try:
                 id = int(id)
             except ValueError:
                 return self.get_json_file_content("INTERNAL_ERR.json")
             username = self.session.get_username()
             task_del = self.modele.del_task_id(username, id);
             if task_del == None:
                 return self.get_json_file_content("INTERNAL_ERR.json")
             return self.get_json_file_content("TASK_ID_DEL_RES.json")
         else:
             return self.get_json_file_content("LOGGED_ERR.json")

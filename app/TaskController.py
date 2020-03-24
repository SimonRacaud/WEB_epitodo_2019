# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-24T11:52:07+01:00

from flask import render_template
from flask import jsonify
from flask import json
from datetime import datetime

from app import app

class TaskController:

    def __init__(self):
        raise Exception("Error: class not instanciable")

    def __check_format_datetime(self, argv = dict()):
        if 'begin' in argv and argv['begin'] != None and (argv['begin'] != ""):
            argv['begin'] = self.convert_str_datetime(argv['begin'])
            if argv['begin'] == None:
                print("check format datetime : begin value error")
                return None
            argv['begin'] = str(argv['begin'])
        elif ('begin' in argv) and (argv['begin'] == ""):
            argv['begin'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if ('end' in argv) and (argv['end'] != None) and (argv['end'] != ""):
            argv['end'] = self.convert_str_datetime(argv['end'])
            if argv['end'] == None:
                print("check format datetime : end value error")
                return None
            argv['end'] = str(argv['end'])
        elif ('end' in argv) and (argv['end'] == ""):
            argv['end'] = None
        return True

    def __check_status_value(self, status = str()):
        valid_values = ['not started', 'in progress', 'done']
        if status in valid_values:
            return True
        return None

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
            id = self.get_int_id(id)
            if id == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            username = self.session.get_username()
            task = self.modele.get_task_id(username, id);
            if task == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            elif task == False:
                return self.get_json_file_content("TASK_ID_ERR.json")
            ret = dict()
            ret["title"] = task["title"]
            ret["begin"] = str(task["begin"])
            ret["end"] = str(task["end"])
            ret["status"] = task["status"]
            return jsonify(result = ret)
        else:
            return self.get_json_file_content("LOGGED_ERR.json")

    def task_update_with_id(self, id, argv = dict()):
        if self.is_logged():
            id = self.get_int_id(id)
            ret_time = self.__check_format_datetime(argv)
            ret_stat = self.__check_status_value(argv['status'])
            if id == None or len(argv) == 0 or ret_stat == None or ret_time == None:
                print("task_update_with_id : ERR argument value")
                return self.get_json_file_content("INTERNAL_ERR.json")
            username = self.session.get_username()
            task_update = self.modele.upd_task_id(username, id, argv);
            if task_update == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            elif task_update == False:
                return self.get_json_file_content("TASK_ID_ERR.json")
            return self.get_json_file_content("TASK_ID_MOD_RES.json")
        else:
            return self.get_json_file_content("LOGGED_ERR.json")

    def task_set_new(self, argv = dict()):
        if self.is_logged():
            ret_time = self.__check_format_datetime(argv)
            ret_stat = self.__check_status_value(argv['status'])
            if len(argv) == 0 or ret_time == None or ret_stat == None:
                print("task_set_new : ERR argument value")
                return self.get_json_file_content("INTERNAL_ERR.json")
            username = self.session.get_username()
            task_add = self.modele.set_task(username, argv);
            if task_add == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            elif task_add == False:
                return self.get_json_file_content("TASK_ID_ERR.json")
            return self.get_json_file_content("TASK_ID_ADD_RES.json")
        else:
            return self.get_json_file_content("LOGGED_ERR.json")

    def task_del_with_id(self, id):
         if self.is_logged():
             id = self.get_int_id(id)
             if id == None:
                 return self.get_json_file_content("INTERNAL_ERR.json")
             username = self.session.get_username()
             task_del = self.modele.del_task_id(username, id);
             if task_del == None:
                 return self.get_json_file_content("INTERNAL_ERR.json")
             elif task_del == False:
                return self.get_json_file_content("TASK_ID_ERR.json")
             return self.get_json_file_content("TASK_ID_DEL_RES.json")
         else:
             return self.get_json_file_content("LOGGED_ERR.json")

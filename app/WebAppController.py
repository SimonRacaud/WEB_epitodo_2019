# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-24T11:52:07+01:00

from flask import render_template
from flask import redirect
from datetime import datetime

from app import app

class WebAppController:

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

    def get_tasks_page(self):
        if self.is_logged():
            username = self.session.get_username()
            tasks = self.modele.get_task_all(username)
            if tasks == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            list_task = list()
            for task in tasks:
                element = dict()
                if task['title'] != "":
                    element["title"] = task["title"]
                else:
                    element['title'] = "Unamed"
                if str(task["begin"]) != "None":
                    element["begin"] = str(task["begin"])
                else:
                    element["begin"] = "Undefined"
                if str(task["end"]) != "None":
                    element["end"] = str(task["end"])
                else:
                    element["end"] = "Undefined"
                element["status"] = task["status"]
                element["id"] = task["task_id"]
                list_task.append(element)
            res = dict()
            res["tasks"] = list_task
            return render_template("tasks.html", result = res, length = len(res['tasks']))
        else:
            return render_template("login.html")

    def get_home_page(self):
        if self.is_logged():
            return self.get_tasks_page()
        else:
            return render_template("login.html")

    def get_signout_page(self):
        if self.is_logged():
            return render_template("signout.html")
        else:
            return render_template("login.html")

    def get_task_add_page(self):
        if self.is_logged():
            return render_template("add_task.html")
        else:
            return render_template("login.html")

    def delete_and_get_tasks_page(self, id):
         if self.is_logged():
             id = self.get_int_id(id)
             if id == None:
                 return self.get_json_file_content("INTERNAL_ERR.json")
             username = self.session.get_username()
             task_del = self.modele.del_task_id(username, id)
             if task_del == None:
                 return self.get_json_file_content("INTERNAL_ERR.json")
             elif task_del == False:
                return self.get_json_file_content("TASK_ID_ERR.json")
             return redirect("/tasks_page")
         else:
             return render_template("login.html")

    def update_and_get_tasks_page(self, id, argv = dict()):
        if self.is_logged():
            id = self.get_int_id(id)
            ret_time = self.__check_format_datetime(argv)
            ret_stat = self.__check_status_value(argv['status'])
            if id == None or len(argv) == 0 or ret_stat == None or ret_time == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            username = self.session.get_username()
            task_update = self.modele.upd_task_id(username, id, argv)
            if task_update == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            elif task_update == False:
                return self.get_json_file_content("TASK_ID_ERR.json")
            return redirect("/tasks_page")
        else:
            return render_template("login.html")

    def get_update_page(self, id):
        if self.is_logged():
            id = self.get_int_id(id)
            if id == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            username = self.session.get_username()
            task = self.modele.get_task_id(username, id)
            if task == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            elif task == False:
                return self.get_json_file_content("TASK_ID_ERR.json")
            ret = dict()
            ret["title"] = task["title"]
            ret["begin"] = str(task["begin"])
            if str(task['end']) != "None":
                ret["end"] = str(task["end"])
            else:
                ret["end"] = ""
            ret["status"] = task["status"]
            return render_template("update.html", result = ret, id = id)
        else:
            return render_template("login.html")

    def apply_new_task(self, argv = dict()):
        if self.is_logged():
            ret_time = self.__check_format_datetime(argv)
            ret_stat = self.__check_status_value(argv['status'])
            if len(argv) == 0 or ret_time == None or ret_stat == None:
                print("task_set_new : ERR argument value")
                return self.get_json_file_content("INTERNAL_ERR.json")
            username = self.session.get_username()
            task_add = self.modele.set_task(username, argv)
            if task_add == None:
                return self.get_json_file_content("INTERNAL_ERR.json")
            elif task_add == False:
                return self.get_json_file_content("TASK_ID_ERR.json")
            return redirect("/add_task_page")
        else:
            return render_template("login.html")
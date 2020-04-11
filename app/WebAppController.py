# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-04-11T17:36:45+02:00

from flask import render_template
from flask import redirect
from datetime import datetime

from app import app

class WebAppController:

    def get_tasks_page(self):
        if self.is_logged():
            username = self.session.get_username()
            tasks = self.modele.get_task_all(username)
            if tasks == None:
                return render_template("error.html")
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

    def get_debug_page(self):
        return render_template("debug.html")

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
                 return render_template("error.html")
             username = self.session.get_username()
             task_del = self.modele.del_task_id(username, id)
             if task_del == None:
                 return render_template("error.html")
             elif task_del == False:
                return render_template("error.html")
             return redirect("/tasks_page")
         else:
             return render_template("login.html")

    def update_and_get_tasks_page(self, id, argv = dict()):
        if self.is_logged():
            id = self.get_int_id(id)
            ret_time = self.check_format_datetime(argv)
            ret_stat = self.check_status_value(argv['status'])
            if id == None or len(argv) == 0 or ret_stat == None or ret_time == None:
                return render_template("error.html")
            username = self.session.get_username()
            task_update = self.modele.upd_task_id(username, id, argv)
            if task_update == None:
                return render_template("error.html")
            elif task_update == False:
                return render_template("error.html")
            return redirect("/tasks_page")
        else:
            return render_template("login.html")

    def get_update_page(self, id):
        if self.is_logged():
            id = self.get_int_id(id)
            if id == None:
                return render_template("error.html")
            username = self.session.get_username()
            task = self.modele.get_task_id(username, id)
            if task == None:
                return render_template("error.html")
            elif task == False:
                return render_template("error.html")
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
            ret_time = self.check_format_datetime(argv)
            ret_stat = self.check_status_value(argv['status'])
            if len(argv) == 0 or ret_time == None or ret_stat == None:
                return render_template("error.html")
            username = self.session.get_username()
            task_add = self.modele.set_task(username, argv)
            if task_add == None:
                return render_template("error.html")
            elif task_add == False:
                return render_template("error.html")
            return redirect("/add_task_page")
        else:
            return render_template("login.html")

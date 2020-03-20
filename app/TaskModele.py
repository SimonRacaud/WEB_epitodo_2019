# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-20T17:53:22+01:00

from .DataBase import DataBase

from app import controller

class TaskModele:

    def __init__(self):
        raise Exception("Error: not instanciable class")

    def __get_user_id(self, username):
        query = "SELECT user_id FROM user WHERE username=%s"
        user = self.db.query(query, [username], True)
        if user == None or len(user) != 1:
            return None
        return user[0]["user_id"]

    def __get_tasks_id_of_user(self, user_id):
        query = "SELECT fk_task_id FROM user_has_task WHERE fk_user_id=%s"
        tasks_id = self.db.query(query, [user_id], True)
        if tasks_id == None:
            return None
        return tasks_id

    def __get_task_width_id(self, task_id):
        query = "SELECT * FROM task WHERE task_id=%s"
        data = self.db.query(query, [task_id], True)
        if data == None:
            return None
        return data[0]

    def get_task_all(self, username):
        user_id = self.__get_user_id(username)
        if user_id == None:
            print("get_task_all : can't get user id")
            return None
        tasks_id = self.__get_tasks_id_of_user(user_id)
        if tasks_id == None:
            print("get_task_all : can't get tasks id")
            return None
        task_list = list()
        for id in tasks_id:
            task = self.__get_task_width_id(id['fk_task_id'])
            if task == None:
                print("get_task_all : can't get task content")
                return None
            else:
                task_list.append(task)
        return task_list

    def get_task_id(self, username, id):
        user_id = self.__get_user_id(username)
        if user_id == None:
            print("get_task_all : can't get user id")
            return None
        tasks_id = self.__get_tasks_id_of_user(user_id)
        if tasks_id == None:
            print("get_task_all : can't get tasks id")
            return None
        if controller.is_id_in_tasks_id(id, tasks_id):
            task = self.__get_task_width_id(id)
            if task == None:
                print("get_task_id : can't get task content")
                return None
            return task
        print("get_task_id : task not found")
        return list()

    def upd_task_id(self, username, id):
        pass

    def set_task(self, username):
        pass

    def del_task_id(self, username, id):
        pass

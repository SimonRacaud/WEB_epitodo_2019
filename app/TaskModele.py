# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-20T18:21:34+01:00

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

    def __update_task_width_id(self, tasks_id, argv):
        if len(argv) != 4:
            return False
        argv.append(task_id)
        query = "UPDATE task SET title=%s, begin=%s, end=%s, status=%s WHERE task_id=%s"
        ret = self.db.query(query, argv, False)
        if ret == None:
            return False
        return True

    def __get_task_user_id(self, username):
        user_id = self.__get_user_id(username)
        if user_id == None:
            print("in TaskModele : can't get user id")
            return None
        tasks_id = self.__get_tasks_id_of_user(user_id)
        if tasks_id == None:
            print("in TaskModele : can't get tasks id")
            return None
        return (user_id, tasks_id)

    def get_task_all(self, username):
        user_id, tasks_id = self.__get_task_user_id(username)
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
        user_id, tasks_id = self.__get_task_user_id(username)
        if controller.is_id_in_tasks_id(id, tasks_id):
            task = self.__get_task_width_id(id)
            if task == None:
                print("get_task_id : can't get task content")
                return None
            return task
        print("get_task_id : task not found")
        return list()

    def upd_task_id(self, username, id, argv):
        user_id, tasks_id = self.__get_task_user_id(username)
        if controller.is_id_in_tasks_id(id, tasks_id):
            if self.__update_task_width_id(id, argv):
                return True
            else:
                print("upd_task_id : cannot update task")
                return None
        print("upd_task_id : task not found")
        return None

    def set_task(self, username, argv):
        user_id = self.__get_user_id(username)
        if user_id == None:
            print("set_task : can't get user id")
            return None
        # set task in db
        # set task_id:user_id in user_has_task

    def del_task_id(self, username, id):
        # get user id
        # try to remove task_id in task
        # remove entries width task_id in user_has_task
        pass

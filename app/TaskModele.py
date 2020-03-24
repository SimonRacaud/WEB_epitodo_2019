# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-24T11:25:43+01:00

from .DataBase import DataBase

from app import controller

class TaskModele:

    def __init__(self):
        raise Exception("Error: not instanciable class")

    ## Get the user_id of an user
    def __get_user_id(self, username):
        query = "SELECT user_id FROM user WHERE username=%s"
        user = self.db.query(query, [username], True)
        if user == None or len(user) != 1:
            return None
        return user[0]["user_id"]

    ## Get all the task_id of an user
    def __get_tasks_id_of_user(self, user_id):
        query = "SELECT fk_task_id FROM user_has_task WHERE fk_user_id=%s"
        tasks_id = self.db.query(query, [user_id], True)
        if tasks_id == None:
            return None
        return tasks_id

    ## Get a task width a specific id
    def __get_task_width_id(self, task_id):
        query = "SELECT * FROM task WHERE task_id=%s"
        data = self.db.query(query, [task_id], True)
        if data == None:
            return None
        return data[0]

    ## Update a task width a specific id
    def __update_task_with_id(self, task_id, title, status, begin, end):
        if len(argv) != 4:
            print("__update_task_with_id : invalid len of argv")
            return False
        argv.append(task_id)
        query = "UPDATE task SET title=%s, begin=%s, end=%s, status=%s WHERE task_id=%s"
        ret = self.db.query(query, (title, status, begin, end), False)
        if ret == None:
            return False
        return True

    ## Get the id of an user && all the task_id owned by this user
    def __get_task_and_user_id_with_username(self, username):
        user_id = self.__get_user_id(username)
        if user_id == None:
            print("in TaskModele : can't get user id")
            return None, None
        tasks_id = self.__get_tasks_id_of_user(user_id)
        if tasks_id == None:
            print("in TaskModele : can't get tasks id")
            return None, None
        return (user_id, tasks_id)

    ## Get the max task id (so the last inserted)
    def __get_max_task_id(self):
        query = "SELECT MAX(task_id) FROM task"
        ret = self.db.query(query, [], True)
        if ret == None:
            return None
        return ret[0]['MAX(task_id)']

    ## Insert a new task
    def __insert_task(self, title, status, begin = None, end = None):
        query = "INSERT INTO task (title, begin, end, status) VALUES (%s, %s, %s, %s)"
        ret = self.db.query(query, (title, begin, end, status), False)
        if ret == None:
            return None
        return self.__get_max_task_id()

    ## Insert an entry in user_has_task table.
    def __insert_user_has_task(self, user_id, task_id):
        query = "INSERT INTO user_has_task (fk_user_id, fk_task_id) VALUES (%s, %s)"
        ret = self.db.query(query, [user_id, task_id], False)
        if ret == None:
            return None
        return True

    ## Remove all entries in user_has_task than have a specific task_id
    def __remove_user_hase_task_with_task_id(self, task_id):
        query = "DELETE FROM user_has_task WHERE fk_task_id=%s"
        ret = self.db.query(query, [task_id], False)
        if ret == None:
            return None
        elif ret == False:
            return False
        return True

    ## Remove a task with a specific id
    def __remove_task_with_task_id(self, task_id):
        query = "DELETE FROM task WHERE task_id=%s"
        ret = self.db.query(query, [task_id], False)
        if ret == None:
            return None
        elif ret == False:
            return False
        return True

    ## /user/task
    def get_task_all(self, username):
        user_id, tasks_id = self.__get_task_and_user_id_with_username(username)
        if user_id == None or tasks_id == None:
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

    ## /user/task/id (GET)
    def get_task_id(self, username, id):
        user_id, tasks_id = self.__get_task_and_user_id_with_username(username)
        if user_id == None or tasks_id == None:
            return None
        if controller.is_id_in_tasks_id(id, tasks_id):
            task = self.__get_task_width_id(id)
            if task == None:
                print("get_task_id : can't get task content")
                return None
            return task
        print("get_task_id : task not found")
        return False

    ## /user/task/id (POST)
    def upd_task_id(self, username, id, argv):
        user_id, tasks_id = self.__get_task_and_user_id_with_username(username)
        if user_id == None or tasks_id == None:
            return None
        if controller.is_id_in_tasks_id(id, tasks_id):
            if self.__update_task_with_id(id, argv['title'], argv['status'], argv['begin'], argv['end']):
                return True
            else:
                print("upd_task_id : cannot update task")
                return None
        print("upd_task_id : task not found")
        return False

    ## /user/task/add
    def set_task(self, username, argv):
        user_id = self.__get_user_id(username)
        if user_id == None:
            print("set_task : cannot get user id")
            return None
        task_id = self.__insert_task(argv['title'], argv['status'], argv['begin'], argv['end'])
        if task_id == None:
            print("set_task : fail to insert task in db")
            return None
        ret = self.__insert_user_has_task(user_id, task_id)
        if ret == None:
            print("set_task : fail to insert user_has_task entry in db")
            return None
        return True

    ## /user/task/del/id
    def del_task_id(self, username, id): # remove only tasks of the logged user ?
        """
        user_id = self.__get_user_id(username)
        if user_id == None:
            print("del_task_id : cannot get user id")
            return None
        """
        ret = self.__remove_task_with_task_id(id)
        if ret == None:
            print("del_task_id : fail to remove task")
            return None
        elif ret == False:
            return False
        ret = self.__remove_user_hase_task_with_task_id(id)
        if ret == None:
            print("del_task_id : fail to remove user_has_task entr(y|ies)")
            return None
        return True

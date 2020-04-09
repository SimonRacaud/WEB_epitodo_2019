# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-04-09T17:43:22+02:00

from .DataBase import DataBase

from app import controller

class TaskModele:

    def __init__(self):
        raise Exception("Error: not instanciable class")

    ## Get the user_id of an user
    def __get_user_id(self, username):
        query = "SELECT user_id FROM user WHERE username=%s"
        user = self.db.query_fetchone(query, [username])
        if user == None or len(user) != 1:
            return None
        return user['user_id']

    ## Get the max task id (so the last inserted)
    def __get_max_task_id(self):
        query = "SELECT MAX(task_id) FROM task"
        ret = self.db.query_fetchone(query, [])
        if ret == None:
            return None
        return ret['MAX(task_id)']

    ## Insert a new task
    def __insert_task(self, title, status, begin = None, end = None):
        query = "INSERT INTO task (title, begin, end, status) VALUES (%s, %s, %s, %s)"
        ret = self.db.query(query, (title, begin, end, status), True)
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
    def __remove_user_hase_task_with_task_id(self, task_id, user_id):
        query = "DELETE FROM user_has_task WHERE fk_task_id=%s AND fk_user_id=%s"
        ret = self.db.query(query, [task_id, user_id], False)
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
        query = "SELECT task_id, title, begin, end, status FROM task INNER JOIN user_has_task ON user_has_task.fk_task_id=task.task_id AND user_has_task.fk_user_id=%s"
        user_id = self.__get_user_id(username)
        if user_id == None:
            return None
        ret = self.db.query(query, [user_id], True)
        if ret == None:
            print("get_task_all : Fail to get all tasks")
            return None
        return ret

    ## /user/task/id (GET)
    def get_task_id(self, username, id):
        query = ("SELECT task_id, title, begin, end, status"
                " FROM task"
                " INNER JOIN user_has_task"
                " ON"
                " user_has_task.fk_task_id=task.task_id"
                " AND"
                " user_has_task.fk_user_id=%s"
                " AND"
                " user_has_task.fk_task_id=%s")
        user_id = self.__get_user_id(username)
        if user_id == None:
            return None
        task = self.db.query_fetchone(query, [user_id, id])
        if task == None:
            print("get_task_id : Fail to get task task_id = ", id, ", user_id = ", user_id)
            return None
        return task

    ## /user/task/id (POST)
    def upd_task_id(self, username, id, argv):
        query = ("UPDATE task INNER JOIN user_has_task"
                " ON user_has_task.fk_task_id=task.task_id"
                " AND user_has_task.fk_user_id=%s"
                " AND user_has_task.fk_task_id=%s"
                " SET title=%s, begin=%s, end=%s, status=%s")
        user_id = self.__get_user_id(username)
        if user_id == None:
            return None
        ret = self.db.query(query, [user_id, id, argv['title'], argv['begin'], argv['end'], argv['status']])
        if ret != True:
            print("upd_task_id : cannot update task")
            return None
        return True

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
    def del_task_id(self, username, id):
        user_id = self.__get_user_id(username)
        if user_id == None:
            print("del_task_id : cannot get user id")
            return None
        ret = self.__remove_user_hase_task_with_task_id(id, user_id)
        if ret == None:
            print("del_task_id : fail to remove user_has_task entr(y|ies)")
            return None
        elif ret == False:
            print("del_task_id : fail to remove, the user is not the owner")
        ret = self.__remove_task_with_task_id(id)
        if ret == None:
            print("del_task_id : fail to remove the task entry")
            return None
        return True

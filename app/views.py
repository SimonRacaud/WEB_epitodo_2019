# @Author: simon
# @Date:   2020-03-18T13:40:03+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-21T09:57:10+01:00

from flask import request
from app import app
from app import controller
from .controller import AppController

controller = AppController()

"""
    INDEX
"""
@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def route_index():
    """ Home page """
    return controller.get_home_page()

"""
    USER
"""
@app.route('/register', methods = ['POST'])
def route_user_register():
    username = request.form['key1']
    password = request.form['key2']
    return controller.register(username, password)

@app.route('/signin', methods = ['POST'])
def route_user_signin():
    username = request.form['username']
    password = request.form['password']
    return controller.signin(username, password)

@app.route('/signout', methods = ['POST'])
def route_user_signout():
    return controller.signout()

@app.route('/user', methods = ['GET'])
def route_user_information():
    return controller.get_information()

"""
    TASKs
"""
@app.route('/user/task', methods = ['GET'])
def route_task_get_list():
    return controller.task_get_all()

@app.route('/user/task/<id>', methods = ['GET'])
def route_task_get(id):
    return controller.task_get_with_id(id)

@app.route('/user/task/<id>', methods = ['POST'])
def route_task_update(id):
    return controller.task_update_with_id(id, [])

@app.route('/user/task/add', methods = ['POST'])
def route_task_add():
    return controller.task_set_new([])

@app.route('/user/task/del/<id>', methods = ['POST'])
def route_task_remove(id):
    return controller.task_del_with_id(id)

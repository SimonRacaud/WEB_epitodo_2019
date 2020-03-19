# @Author: simon
# @Date:   2020-03-18T13:40:03+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-19T16:46:55+01:00

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
    return "Get list of all users\n"

@app.route('/user/task/<id>', methods = ['GET'])
def route_task_get(id):
    return "Get specific task: id=[" + id + "]\n"

@app.route('/user/task/<id>', methods = ['POST'])
def route_task_update(id):
    return "Update specific task: id=[" + id + "]\n"

@app.route('/user/task/add', methods = ['POST'])
def route_task_add():
    return "Add a new task\n"

@app.route('/user/task/del/<id>', methods = ['POST'])
def route_task_remove(id):
    return "Remove a task : id=[" + id + "]\n"

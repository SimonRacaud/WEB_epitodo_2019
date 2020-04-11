# @Author: simon
# @Date:   2020-03-18T13:40:03+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-04-11T17:51:02+02:00

from flask import request
from flask import redirect
from app import app
from app import controller
from .controller import AppController
from flask import json

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
    DEBUG
"""
@app.route('/debug', methods = ['GET'])
def route_debug_index():
    """ Debug page """
    return controller.get_debug_page()

"""
    USER
"""
@app.route('/register', methods = ['POST'])
def route_user_register():
    try:
        username = request.form['username']
        password = request.form['password']
    except Exception:
        username = None
        password = None
    return controller.register(username, password)

@app.route('/signin', methods = ['POST'])
def route_user_signin():
    try:
        username = request.form['username']
        password = request.form['password']
    except Exception:
        username = None
        password = None
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
    argv = dict()
    try:
        argv['begin'] = request.form['begin']
    except Exception:
        argv['begin'] = None
    try:
        argv['end'] = request.form['end']
    except Exception:
        argv['end'] = None
    try:
        argv['title'] = request.form['title']
        argv['status'] = request.form['status']
    except Exception:
        argv = dict()
    return controller.task_update_with_id(id, argv)

@app.route('/user/task/add', methods = ['POST'])
def route_task_add():
    argv = dict()
    try:
        argv['begin'] = request.form['begin']
    except Exception:
        argv['begin'] = None
    try:
        argv['end'] = request.form['end']
    except Exception:
        argv['end'] = None
    try:
        argv['title'] = request.form['title']
        argv['status'] = request.form['status']
    except Exception:
        argv = dict()
    return controller.task_set_new(argv)

@app.route('/user/task/del/<id>', methods = ['POST'])
def route_task_remove(id):
    return controller.task_del_with_id(id)

"""
    WEBAPP
"""

@app.route('/add_task_page', methods = ['GET'])
def route_add_task_page():
    return controller.get_task_add_page()

@app.route('/tasks_page', methods = ['GET'])
def route_tasks_page():
    return controller.get_tasks_page()

@app.route('/signin_redirect', methods = ['POST'])
def route_user_signin_redirect():
    route_user_signin()
    return redirect('/')

@app.route('/register_redirect', methods = ['POST'])
def route_user_register_redirect():
    route_user_register()
    return redirect('/')

@app.route('/signout_redirect', methods = ['POST'])
def route_user_signout_redirect():
    route_user_signout()
    return redirect('/')

@app.route('/signout_page', methods = ['GET'])
def route_signout_page():
    return controller.get_signout_page()

@app.route('/delete_task/<id>', methods = ['POST'])
def route_delete_task(id):
    return controller.delete_and_get_tasks_page(id)

@app.route('/update_page/<id>', methods = ['GET'])
def route_update_page(id):
    return controller.get_update_page(id)

@app.route('/update_task/<id>', methods = ['POST'])
def route_update_task(id):
    argv = dict()
    try:
        argv['begin'] = request.form['begin']
    except Exception:
        argv['begin'] = None
    try:
        argv['end'] = request.form['end']
    except Exception:
        argv['end'] = None
    try:
        argv['title'] = request.form['title']
        argv['status'] = request.form['status']
    except Exception:
        argv = dict()
    return controller.update_and_get_tasks_page(id, argv)

@app.route('/add_task', methods = ['POST'])
def route_add_task():
    argv = dict()
    try:
        argv['begin'] = request.form['begin']
    except Exception:
        argv['begin'] = None
    try:
        argv['end'] = request.form['end']
    except Exception:
        argv['end'] = None
    try:
        argv['title'] = request.form['title']
        argv['status'] = request.form['status']
    except Exception:
        argv = dict()
    return controller.apply_new_task(argv)

# @Author: simon
# @Date:   2020-03-18T13:40:03+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-18T18:47:58+01:00

from app import app
from app import controller
from .controller import User_controller

"""
    INDEX
"""
@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def route_index():
    """ Home page """
    #render_template("index2.html", title="TEST", content="Content")
    return "Home page (TEMP DEBUG)\n"

"""
    USER
"""
@app.route('/register', methods = ['POST'])
def route_user_register():
    #username = request.form['key1']
    return "Register user\n"

@app.route('/signin', methods = ['POST'])
def route_user_signin():
    return "Login user\n"

@app.route('/signout', methods = ['POST'])
def route_user_signout():
    return "Logout user\n"

@app.route('/user', methods = ['GET'])
def route_user_information():
    controller = User_controller()
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

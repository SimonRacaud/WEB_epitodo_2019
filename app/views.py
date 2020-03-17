from app import app

@app.route('/', methods =['GET'])

@app.route('/index', methods =['GET'])
def route_home():
    return "Hello world!\n"

@app.route('/user/<username>', methods =['POST', 'GET'])
def route_add_user(username):
    return "User added!\n"

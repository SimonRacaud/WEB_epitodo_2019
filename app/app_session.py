# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-20T13:59:20+01:00

from flask import session

from app import app

class AppSession:

    def __init__(self):
        pass

    def exist(self):
        if session.get('username') == None:
            return False
        else:
            return True

    def set_session(self, username):
        if isinstance(username, str):
            if self.exist():
                print("AppSession : session already exist")
            else:
                print("New username " + username)
                session['username'] = username
                print("AppSession: Session created")
                return True
        else:
            print("Warning: AppSession::set_session : invalid type of arg")
        return False

    def del_session(self):
        if self.exist():
            session.pop('username', None)
            session['username'] = None
            print("AppSession: session destroy")
            return True
        else:
            print("Warning: AppSession::del_session : session doesn't exist")
        return False

    def get_username(self):
        if self.exist():
            return session.get('username')
        else:
            print("Warning: AppSession::get_username : session doesn't exist")
        return None

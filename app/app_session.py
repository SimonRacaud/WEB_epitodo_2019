# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-19T16:52:30+01:00

from flask import session
from flask_session import Session
from datetime import timedelta

from app import app

class AppSession:

    def __init__(self):
        app.permanent_session_lifetime = timedelta(hours = 1)
        self.session = Session()
        self.session.init_app(app)

    def is_logged(self):
        if session.get("username") is None:
            return True
        else:
            return False

    def set_session(self, username):
        if isinstance(username, str) and isinstance(password, str):
            if not self.is_logged():
                session['username'] = username
                print("AppSession: Session created")
                return True
            else:
                print("Warning: Session already exist")
        else:
            print("Warning: AppSession::set_session : invalid type of arg")
        return False

    def del_session(self):
        if self.is_logged():
            session.pop('username', None)
            print("AppSession: session destroy")
            return True
        else:
            print("Warning: AppSession::del_session : session doesn't exist")
        return False

    def get_username(self):
        if 'username' in session:
            return session.get('username')
        else:
            print("Warning: AppSession::get_username : session doesn't exist")
        return None

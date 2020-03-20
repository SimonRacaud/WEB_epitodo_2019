# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-20T15:01:55+01:00

class UserModele:

    def __init__(self):
        raise Exception("Error: not instanciable class")

    def user_exist(self, username, password = None):
        parameters = [username]
        if not password is None:
            query = "SELECT user_id FROM user WHERE username=%s AND password=%s"
            parameters.append(password)
        else:
            query = "SELECT user_id FROM user WHERE username=%s"
        result = self.db.query(query, parameters, True)
        if result == None:
            return None
        if len(result) == 0:
            return False
        return True

    def get_info(self, username):
        query = "SELECT user_id, username, password, logged FROM user WHERE username=%s"
        result = self.db.query(query, [username], True)
        if result == None:
            return None
        if len(result) == 0:
            return None
        return result[0]

    def signin(self, username, password):
        ret = self.user_exist(username, password)
        if ret != True:
            return ret
        query = "UPDATE user SET logged=True WHERE username=%s"
        ret = self.db.query(query, [username], False)
        if ret == None:
            return None
        return True

    def signout(self, username):
        ret = self.user_exist(username)
        if ret != True:
            return ret
        query = "UPDATE user SET logged=False WHERE username=%s"
        ret = self.db.query(query, [username], False)
        if ret == None:
            return None
        return True

    def register(self, username, password):
        ret = self.user_exist(username)
        if ret == True:
            return False
        elif ret == None:
            return None
        query = "INSERT INTO user(username, password) VALUES (%s, %s)"
        ret = self.db.query(query, [username, password], False)
        if ret == None:
            return None
        return True

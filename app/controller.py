# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: PROJECT_NAME
# @Last modified by:   simon
# @Last modified time: 2020-03-18T18:48:06+01:00


from app import models
from .models import User_modele

class Task_controller:

    def __init__(self):
        self.modele = Task_modele()

    def get_all(self):
        pass

    def get_with_id(self):
        pass

    def set_with_id(self):
        pass

    def set_new(self):
        pass

    def del_with_id(self):
        pass

class User_controller:

    def __init__(self):
        self.modele = User_modele()
        #self.session = Session(self.modele)

    def get_information(self):
        data = self.modele.get_info()
        print(data)
        return "Get list of user informations\n"

class Session:

    def __init__(self):
        pass

    def is_logged(self):
        pass

    def login(self):
        pass

    def logout(self):
        pass

    def register(self):
        pass

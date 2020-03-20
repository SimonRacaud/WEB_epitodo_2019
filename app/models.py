# @Author: simon
# @Date:   2020-03-17T15:19:40+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-20T14:54:33+01:00

from .DataBase import DataBase

from .TaskModele import TaskModele
from .UserModele import UserModele

class AppModele(UserModele, TaskModele):
    """
        AppModele class:

        #
        # Send requets to the database (update, get or set data)
        #

        - UserModele : function that manage all about users
        - TaskModele : function that manage all about tasks of the users
    """
    def __init__(self):
        self.db = DataBase()

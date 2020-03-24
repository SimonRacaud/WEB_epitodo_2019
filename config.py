# @Author: simon
# @Date:   2020-03-17T15:19:34+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-24T11:39:01+01:00

from datetime import timedelta

DATABASE_NAME = "epytodo"

DATABASE_HOST = "localhost"

DATABASE_SOCK = "/run/mysqld/mysqld.sock"

DATABASE_USER = "root"

DATABASE_PASS = "root"

SECRET_KEY = 'I_love_cookies'

PERMANENT_SESSION_LIFETIME = timedelta(minutes=8)

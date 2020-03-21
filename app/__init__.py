# @Author: simon
# @Date:   2020-03-18T13:40:03+01:00
# @Project: WEB_epytodo_2019
# @Last modified by:   simon
# @Last modified time: 2020-03-21T08:50:09+01:00

from flask import Flask
import os

app = Flask(__name__)
app.config.from_object('config')

from app import views

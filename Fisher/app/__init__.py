# @Time    : 2018-10-27 23:00
# @Author  : DuQing
# @File    : __init__.py.py
"""
description
"""
from flask import Flask

from app.web.book import web


def create_app():
    app = Flask(__name__)
    app.register_blueprint(web)
    return app
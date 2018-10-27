# @Time    : 2018-10-27 23:01
# @Author  : DuQing
# @File    : book.py
"""
description
"""
from flask import jsonify, Blueprint

from helper import is_isbn_or_key
from app.web.yushu_book import YuShuBook


web = Blueprint('web', __name__)
@web.route('/book/search/<q>/<page>')
def book_search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        res = YuShuBook.search_by_isbn(q)
    else:
        res = YuShuBook.search_by_key(q)
    return jsonify(res)

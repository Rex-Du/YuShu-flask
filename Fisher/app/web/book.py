# @Time    : 2018-10-27 23:01
# @Author  : DuQing
# @File    : book.py
"""
description
"""
from flask import jsonify, Blueprint, request

from helper import is_isbn_or_key
from app.web.yushu_book import YuShuBook
from app.forms.book import SearchForm


web = Blueprint('web', __name__)
@web.route('/book/search')
def book_search():
    # request   localhost:8888/book/search?q=9787501524044
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            res = YuShuBook.search_by_isbn(q)
        else:
            res = YuShuBook.search_by_key(q)
        return jsonify(res)
    else:
        return jsonify(form.errors)

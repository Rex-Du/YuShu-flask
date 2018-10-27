# @Time    : 2018-10-27 22:45
# @Author  : DuQing
# @File    : yushu_book.py
"""
description
"""
from http_handle import Http


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        res = Http.get(url)
        return res

    @classmethod
    def search_by_key(cls, key, count=15, start=0):
        url = cls.keyword_url.format(key, count, start)
        res = Http.get(url)
        return res
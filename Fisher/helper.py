# @Time    : 2018-10-27 22:16
# @Author  : DuQing
# @File    : helper.py
"""
description
"""


def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    sort_word = word.replace('-', '')
    if '-' in word and len(sort_word) == 10 and sort_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key

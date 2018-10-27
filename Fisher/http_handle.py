# @Time    : 2018-10-27 22:21
# @Author  : DuQing
# @File    : http_handle.py
"""
搜索书本的api
http://t.yushu.im/v2/book/isbn/{isbn}
http://t.yushu.im/v2/book/isbn/9787501524044
"""
import requests


class Http:
    @staticmethod
    def get(url, return_json=True):
        res = requests.get(url)
        if res.status_code != 200:
            return {} if return_json else ''
        return res.json() if return_json else res.text

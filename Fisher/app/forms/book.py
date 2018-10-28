# @Time    : 2018-10-28 15:51
# @Author  : DuQing
# @File    : book.py
"""
使用wtforms做参数的验证
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30), DataRequired()], default='')
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
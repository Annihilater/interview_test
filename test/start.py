#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-07 17:07
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : start.py
from config import form_data, url
from libs import form_to_dict
from libs.httper import make_session

new_form_data = form_to_dict(form_data)

session = make_session()
response = session.get(url)
with open('context.html', 'w') as f:
    f.write(response.text)

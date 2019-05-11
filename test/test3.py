#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-08 13:51
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test3.py
from test.add_to_excel import add_to_excel

add_to_excel('../article.xlsx', data=['1', 'title', 'url', 'typ', 'publish_time', 'article_id', 'Compliance'])

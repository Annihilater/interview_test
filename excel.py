#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-08 13:01
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : excel.py
from libs.save_to_excel import write_to_excel

excel_title_list = ['id', 'title', 'url', 'typ', 'publish_time', 'article_id', 'Compliance']
file_path = '/Users/stefanannihilater/Dropbox/PycharmProjects/interview_test/data/article.xls'
with open('tmp.txt', 'r') as f:
    data = f.readlines()
# print(data)

new_data = []
for d in data:
    if d is not None:
        t = eval(d)
        new_data.append(t)
# print(new_data)
write_to_excel(excel_title_list, file_path, new_data)

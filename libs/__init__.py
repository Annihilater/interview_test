#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-07 18:12
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : __init__.py.py
from config import form_data


def form_to_dict(raw):
    tmp_list = raw.split("&")
    tmp_dict = {}

    for i in tmp_list:
        tmp = i.split("=")
        tmp_dict[tmp[0]] = tmp[1]

    return tmp_dict


if __name__ == '__main__':
    new_form_data = form_to_dict(form_data)
    print(new_form_data)

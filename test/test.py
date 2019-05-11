#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-08 08:51
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test.py
import datetime


def gen_now_time():
    now = datetime.datetime.now()
    x = now.strftime('%Y/%m/%d %H:%M')
    return x


print(gen_now_time())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-08 08:55
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test2.py
import datetime


def modify_time(t):
    new = ''
    if '小時前' in t:
        t = t.replace('小時前', '')
        hours = int(t)
        now = datetime.datetime.now()
        delta = datetime.timedelta(hours=-hours)
        n_hours = now + delta
        new = n_hours.strftime('%Y/%m/%d %H:%M')
    if '天前' in t:
        t = t.replace('天前', '')
        days = int(t)
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=-days)
        n_days = now + delta
        new = n_days.strftime('%Y/%m/%d %H:%M')
    return new


modify_time('8小時前')

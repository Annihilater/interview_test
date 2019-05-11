#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-08 16:11
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test4.py
import requests

proxy = {'HTTP': 'HTTP://59.49.129.60:8998'}
proxies = {'http': None, 'https': None}
# r = requests.get('http://ip.cip.cc/', proxies=proxy)
r = requests.get('https://httpbin.org/get?show_env=1', proxies=proxy)
print(r.text)

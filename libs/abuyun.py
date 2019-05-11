#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-08 16:34
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : abuyun.py

import requests

from libs.httper import baidu_make_session


def abuyun(url):
    # 要访问的目标页面
    targetUrl = url
    # targetUrl = "http://proxy.abuyun.com/switch-ip"
    # targetUrl = "http://proxy.abuyun.com/current-ip"

    # 代理服务器
    proxyHost = "http-pro.abuyun.com"
    proxyPort = "9010"

    # 代理隧道验证信息
    # 该验证信息已经失效，请更新
    proxyUser = "HUN3392PK841774P"
    proxyPass = "4DCC4081A754940C"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }
    session = baidu_make_session()
    resp = session.get(targetUrl, proxies=proxies)
    # resp = requests.get(targetUrl, proxies=proxies)

    print(resp.status_code)
    # print(resp.text)
    return resp

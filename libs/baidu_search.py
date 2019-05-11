#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-08 10:42
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : baidu_search.py
import urllib
from urllib.parse import quote, urlencode

from bs4 import BeautifulSoup

from libs.abuyun import abuyun
from libs.httper import baidu_make_session


def baidu_search(title):
    base_url = "http://www.baidu.com/s?"
    keyword = quote(title)
    # print(encode_title)
    # wd = urlencode({'wd': keyword})
    # full_url = base_url + wd
    url = 'https://www.baidu.com/s?wd={}&rsv_spt=1&rsv_iqid=0xd81934f7000059b8&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=0&rsv_sug3=2&rsv_t=165fj%2FmdLA%2BtVMpV3E5Or3MDl4e8uTit8TtxCFQF5pELJuu3%2FBz7mLQT8kektVEeM%2BJD&inputT=1786&rsv_sug4=1992'.format(
        keyword
    )
    # session = baidu_make_session()
    # response = session.get(url, proxies=proxies)
    # response = abuyun(full_url)
    response = abuyun(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, features="html.parser")
    ems = soup.find_all('em')  # 百度搜索结果飘红的字段全部在 em 标签内，找出所以的 em 标签并比较 em 标签的长度即可
    compliance = 2
    for em in ems:
        if len(em.text) >= 8:
            # print('相似')
            compliance = 3
    print(ems)
    return compliance


if __name__ == '__main__':
    print(baidu_search('Windows 10 更新送你“魁隆”，装 KB4493509 后随时要重灌！'))

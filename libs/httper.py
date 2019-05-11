#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-07 18:13
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : httper.py
from http.cookies import SimpleCookie

import requests

from config import user_agent, content_type
from libs.gen_timestamp import generate_timestamp


def cookie_to_dict(raw):
    tmp_cookie = SimpleCookie(raw)
    dict_cookies = {i.key: i.value for i in tmp_cookie.values()}
    return dict_cookies


def make_session():
    session = requests.session()
    session.headers.update(
        {"User-Agent": user_agent, "Content-Type": content_type}
    )
    tmp = 't={}&j=0'.format(generate_timestamp())
    cookie = {"B": "2cuorsldutul0&b=3&s=e7", "GUC": "AQEBAQFc0pddtkIj_gUp&s=AQAAAAH7MT6M&g=XNFJmw", "cmp": tmp}
    cookies = cookie_to_dict(cookie)
    requests.utils.add_dict_to_cookiejar(session.cookies, cookie_dict=cookies)
    return session


def baidu_make_session():
    session = requests.session()
    session.headers.update(
        {"User-Agent": user_agent, "Content-Type": content_type}
    )
    cookie = {'BAIDUID': '5248996E6DF457CC2988A62AEDA90160:FG=1', 'BIDUPSID': '5248996E6DF457CC2988A62AEDA90160',
              'PSTM': '1542430790',
              'BDUSS': 'lVfmctfk1zYUZaU1laZDBWcFRDWmViTmxKRUNIRFBoZTZyT3NFekxVRjFsSEJjQVFBQUFBJCQAAAAAAAAAAAEAAABsY6joQW5uaWhpbGF0ZXIzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHUHSVx1B0lcZj',
              'BD_UPN': '123253', 'MCITY': '-%3A', 'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
              'H_PS_PSSID': '26523_1464_28939_21102_18560_28723_28963_28837_28584_28604', 'delPer': '0',
              'BD_CK_SAM': '1', 'PSINO': '5',
              'H_PS_645EC': '3487DXkv7X1POEsG63vm4DssygrZsgjQarGWXXnERFKhhaOZsG1aorLu4p9f6T%2FtX%2BXo', 'BDSVRTM': '0',
              'ZD_ENTRY': 'baidu'}
    cookies = cookie_to_dict(cookie)
    requests.utils.add_dict_to_cookiejar(session.cookies, cookie_dict=cookies)
    return session

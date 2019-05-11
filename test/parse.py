#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-07 18:41
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : parse.py
import re

from bs4 import BeautifulSoup

# with open('context.html', 'r') as f:
#     data = f.read()
from config import base_url
from db import db
from models.article import Article

soup = BeautifulSoup(open('context.html'), features='html.parser')
# print(soup.prettify())
# print(soup.head)
# print(soup.title.text)

articles = soup.find_all(name='div', attrs={'class': 'Ov(h) Pend(44px) Pstart(25px)'})
for article in articles:
    item = {}
    tmp = article.div.text.split('•')
    item['typ'] = tmp[0].strip()
    item['publish_time'] = tmp[1].strip()
    item['title'] = article.a.text
    item['Compliance'] = 1 if len(item['title']) >= 14 else 0
    item['url'] = base_url + article.a['href']
    item['article_id'] = item['url'].split('-')[-1].split('.')[0]
    print(item['article_id'])
    # print(article)

    try:
        if (
                not db.session.query(Article.title).filter_by(title=item["title"]).first()
        ):  # 查不到时，time = None
            with db.auto_commit():
                db.session.add(Article(**item))
            print("写入成功 ok...")
        else:
            print(item["title"], "数据已存在，不写入数据")
    except Exception as e:
        print(item)
    a = 1
# print(soup.body.div.div.div.next_sibling)
# print(soup.find_all('StreamMegaItem'))

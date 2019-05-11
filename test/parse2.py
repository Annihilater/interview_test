#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-07 23:37
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : parse2.py
from config import base_url
from db import db
from models.article import Article

with open('context2.html', 'r') as f:
    data = f.read()


def save_to_mysql(data):
    new_data = eval(data)
    new_data = new_data['data']
    for single in new_data:
        item = {'typ': single['type'], 'publish_time': single['published_at'], 'title': single['title'],
                'url': base_url + single['url'], 'article_id': single['id']}

        item['Compliance'] = 1 if len(item['title']) >= 14 else 0

        try:
            if (
                    not db.session.query(Article.title).filter_by(title=item["title"]).first()
            ):  # 查不到时，time = None
                with db.auto_commit():
                    db.session.add(Article(**item))
                print("写入成功 ok...")
            else:
                print('exist...', "数据已存在，不写入数据", item["title"])
        except Exception as e:
            print('error...', item)

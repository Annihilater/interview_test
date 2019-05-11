#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-08 17:43
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : bug.py
from zhconv import convert

from db import db
from models.article import Article

for i in range(1, 149):
    article = db.session.query(Article).filter_by(id=i).first()
    # print(article)
    article.Compliance = 1 if len(article.title) >= 14 else 0
    single_article = [article.id, article.title, article.url, article.typ, article.publish_time, article.article_id,
                      article.Compliance]

    with open('tmp2.txt', 'a') as f:
        f.write(str(single_article))
        f.write('\n')

    article.title = convert(article.title, 'zh-tw')
    with db.auto_commit():
        db.session.add(article)
    print(i, 'ok...')

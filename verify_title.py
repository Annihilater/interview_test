#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-08 10:19
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : verify_title.py
"""
本文件是将数据库内文章取出来，使用百度搜索验证文章的相似性
相似：Compliance = 3
不相似：Compliance = 2
验证过后将数据写入 tmp.txt 文件，以便下一步写入 excel
"""
from zhconv import convert

from db import db
from libs.baidu_search import baidu_search
from models.article import Article


def verify_title():
    for i in range(1, 149):
        article = db.session.query(Article).filter_by(id=i).first()
        # print(article)
        if article.Compliance == 1:
            article.title = convert(article.title, 'zh-cn')
            article.Compliance = baidu_search(article.title)
            single_article = [article.id, article.title, article.url, article.typ, article.publish_time,
                              article.article_id,
                              article.Compliance]

            with open('/data/tmp.txt', 'a') as f:
                f.write(str(single_article))
                f.write('\n')
            # 将更新好的数据存到数据库
            # with db.auto_commit():
            #     db.session.add(article)
            print(i, 'ok...')
        else:
            print(i, '小于 14')
            continue
            # 如果标题字数小于 14，则不需要验证文章的相似性


if __name__ == '__main__':
    verify_title()

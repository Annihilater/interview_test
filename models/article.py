#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-07 18:47
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : article.py
from sqlalchemy import Column, Integer, String

from models.base import Base


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    url = Column(String(1000))
    typ = Column(String(50))
    publish_time = Column(String(100))
    article_id = Column(String(100))
    Compliance = Column(Integer)
    # 0:标题小于 14
    # 1:标题大于等于 14
    # 2:经过百度相似度验证，不相似
    # 3:经过百度相似度验证，相似

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])

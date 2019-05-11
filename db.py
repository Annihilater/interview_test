#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-07 18:44
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : db.py
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_URI
from models.base import Base


class DB:
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_db_table(self):
        """
        在数据库创建数据表，每个 model 都需要导入一遍才会被创建，否则未使用的表不会在数据库创建
        """
        from models import article

        Base.metadata.create_all(self.engine)

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = DB()

if __name__ == "__main__":
    db.create_db_table()

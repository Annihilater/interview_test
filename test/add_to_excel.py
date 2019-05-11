#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-08 13:13
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : add_to_excel.py
from xlrd import open_workbook
from xlutils.copy import copy


def add_to_excel(file_path, data):
    rexcel = open_workbook(filename=file_path)  # 用wlrd提供的方法读取一个excel文件
    rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
    excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
    row = rows
    column = 0
    for value in data:
        table.write(row, column, value)  # xlwt对象的写方法，参数分别是行、列、值
        column += 1
    excel.save(file_path)  # xlwt对象的保存方法，这时便覆盖掉了原来的excel

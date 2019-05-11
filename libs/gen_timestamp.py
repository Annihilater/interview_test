#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-05-07 23:58
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : gen_timestamp.py
import time


def generate_timestamp():
    t = time.time()
    t = int(round(t))
    return t


if __name__ == "__main__":
    timestamp = generate_timestamp()
    print(timestamp)


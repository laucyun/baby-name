#!/usr/bin/env python
# -*- coding: GB18030 -*-

"""
 Name        : sys_config.py
 Created on  : 2017/06/18 11:28
 Author      : Liuker <liu@liuker.xyz>
 Version     : 1.0.0
 Copyright   : Copyright (C) 2013 - 2017, Liuker's Blog, https://liuker.org.
 Description : 系统的配置。
"""
import os

ROOT_PATH = os.path.join(os.path.dirname(__file__), os.pardir)

# 请求的表单地址
REQUEST_URL = "http://life.httpcn.com/xingming.asp"

# 词典文件路径：男孩，双字名
FPATH_DICTFILE_BOYS_DOUBLE = os.path.abspath(os.path.join(ROOT_PATH, "./dicts/boys_double.txt"))
# 词典文件路径：男孩，单字名
FPATH_DICTFILE_BOYS_SINGLE = os.path.abspath(os.path.join(ROOT_PATH, "./dicts/boys_single.txt"))
# 词典文件路径：女孩，双字名
FPATH_DICTFILE_GIRLS_DOUBLE = os.path.abspath(os.path.join(ROOT_PATH, "./dicts/girls_double.txt"))
# 词典文件路径：女孩，单字名
FPATH_DICTFILE_GIRLS_SINGLE = os.path.abspath(os.path.join(ROOT_PATH, "./dicts/girls_single.txt"))

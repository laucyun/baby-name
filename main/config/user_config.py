#!/usr/bin/env python
# -*- coding: GB18030 -*-

"""
 Name        : user_config.py
 Created on  : 2017/06/18 11:28
 Author      : Liuker <liu@liuker.xyz>
 Version     : 1.0.0
 Copyright   : Copyright (C) 2013 - 2017, Liuker's Blog, https://liuker.org.
 Description : 用户配置。
"""
import os

ROOT_PATH = os.path.join(os.path.dirname(__file__), os.pardir)

setting = {}

# 限定字，如果配置了该值，则会取用单字字典，否则取用多字字典
setting["limit_world"] = "嘉"
# 姓
setting["name_prefix"] = "刘"
# 性别，取值为 男 或者 女
setting["sex"] = "男"
# 省份
setting["area_province"] = "北京"
# 城市
setting["area_region"] = "海淀"
# 出生的公历年份
setting['year'] = "2017"
# 出生的公历月份
setting['month'] = "6"
# 出生的公历日子
setting['day'] = "18"
# 出生的公历小时
setting['hour'] = "18"
# 出生的公历分钟
setting['minute'] = "18"
# 结果产出文件名称
setting['output_fname'] = "example.txt"
setting['output_fpath'] = os.path.abspath(os.path.join(ROOT_PATH, "outputs", setting['output_fname']))

#!/usr/bin/env python
# -*- coding: GB18030 -*-

"""
 Name        : filter.py
 Created on  : 2017/06/18 11:25
 Author      : Liuker <liu@liuker.xyz>
 Version     : 1.0.0
 Copyright   : Copyright (C) 2013 - 2017, Liuker's Blog, https://liuker.org.
 Description : 。
"""

for line in open("../outputs/names_boys_source_wgl_hasguang.txt"):
    name = str(line).strip()
    
    if name == "":
        continue
    
    if "于光" in name:
        print line[:-1]
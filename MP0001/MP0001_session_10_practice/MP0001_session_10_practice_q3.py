#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/28 20:42
@user: jiananwang
@title: MP0001_session_10_practice_q3
"""

import math


all_function_list = dir(math)
legal_function_list = [i for i in all_function_list if i[0] != '_']
legal_function_list_class = [f for f in all_function_list if f.startswith('_') == False]

print(legal_function_list)
print(legal_function_list_class)
print(len(legal_function_list))

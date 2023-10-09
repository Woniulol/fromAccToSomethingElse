#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/24 22:30
@user: jiananwang
@title: MP0001_session_9_practice_q2
"""
import os

print('=' * 5, ' part a ', '=' * 5)
myfile = 'C:\\User\\python\\tmp\\test.py'
print(myfile)
myfile_raw = r'C:\User\python\tmp\test.py'
print(myfile_raw)
print(r'C:\User\python\tmp\test.py')

print('=' * 5, ' part b ', '=' * 5)
sep = os.sep

variable_drive = f'{sep}C'
variabel_dirpath = f'{sep}User{sep}python{sep}tmp{sep}'
variable_filename = 'text.py'
print(variabel_dirpath)
print(f'{variable_drive}:{variabel_dirpath}{variable_filename}')
print(os.path.join(variable_drive, variabel_dirpath, variable_filename))

print('=' * 5, ' part c ', '=' * 5)
print('=' * 5, ' part d ', '=' * 5)

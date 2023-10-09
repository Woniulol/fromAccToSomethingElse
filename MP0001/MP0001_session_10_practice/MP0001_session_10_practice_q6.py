#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/25 23:42
@user: jiananwang
@title: MP0001_session_10_practice_q6
"""

import os
import sys

"""
os.getcwd()
os.lstdir()
os.chdir()
os.path.isdir()
os.path.isfile()
"""

while True:
    target_path = input('please input the target working path: ')
    if os.path.isdir(target_path):
        os.chdir(target_path)
        print("cd successful!", "current wd:", os.getcwd())
        print()
        print('The files and directories available are: ')
        for i in os.listdir():
            print(i)
        print()
        target_file_name = input('Which entry do you wish to get a path on?'
                                 '\ninput here: ')
        print(f'Ok, the full URL is: \n{os.getcwd() + "/" +target_file_name}')
        break

    if target_path == "EXIT":
        sys.exit()
    else:
        print("please try a new path or input EXIT to exit")

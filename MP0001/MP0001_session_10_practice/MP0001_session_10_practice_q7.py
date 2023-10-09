#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/6/28 19:39
@user: jiananwang
@title: MP0001_session_10_practice_q7
"""


def change_file_extension(filename: str, target_extension) -> str:
    filename_name = filename.split('.')[0]

    if target_extension[0] != '.':
        target_extension = "." + target_extension

    return filename_name+target_extension


input_filename = input("please enter the filename: ")
input_target_extension = input("please enter the target extension: ")
print("Your new filename is: ", change_file_extension(input_filename, input_target_extension))



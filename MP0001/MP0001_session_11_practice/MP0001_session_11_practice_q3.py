#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/2 10:40
@user: jiananwang
@title: MP0001_session_11_practice_q3
"""


def input_todo() -> tuple:
    input_date = input('please input the date (YYYY-MM-DD): ')
    input_description = input('please input the description: ')
    input_date = input_date.strip()
    input_description = input_description.strip()
    # import re
    # input_description = re.sub('\t', '', input_description)
    input_description = input_description.replace('\t', ' ')
    return input_date, input_description


def output_todo(to_do):
    import os
    cwd = os.getcwd()
    file_name = 'todo.txt'
    full_file_name = cwd + os.sep + file_name

    fl = open(full_file_name, mode='a', encoding='utf8')
    fl.write(f"{to_do[0]}\t{to_do[1]}\n")  # date + \t + description + \n
    fl.close()

    fl = open(full_file_name, mode='r', encoding='utf8')
    print(fl.read())
    fl.close()


def main():
    to_do = input_todo()
    output_todo(to_do)


if __name__ == '__main__':
    main()

"""
r	以只读方式打开文件；如果文件不存在，则会报错；文件指针将会放在文件的开头。
w	以写入方式打开文件; 打开文件后立即清空文件内所有内容; 如果文件不存在，则会自动创建文件；我们写入内容后，文件指针将会放在文件的末尾。
a	以追加方式打开文件；不会清空原文件内容；如果文件不存在，则会自动创建文件；文件指针将会放在文件的末尾。
r+	除了读取还可以写入，其余同r，需要注意的是文件指针是在开头。
w+	除了写入还可以读取，其余同w，需要注意的是文件指针是在末尾。
a+	除了写入还可以读取，其余同w，需要注意的是文件指针是在末尾。
"""

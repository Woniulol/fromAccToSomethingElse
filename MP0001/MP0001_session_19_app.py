#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/26 12:47
@user: jiananwang
@title: MP0001_session_19_business_app
"""

import os
import time
import numpy as np
import pandas as pd

command_dict = {
    'r': 'batch renaming files',
    'e': 'export file tree',
    'd': 'de-renaming files',
    'm': 'mask files',
    'x': 'exit app'}

len_per_line = 100
separate_line = '-' * len_per_line
side_border = '||'


def my_print(text='', total_space=len_per_line, left_space=5, right_space=5, central=False, index_level=None):
    # automated format print
    # handle all information except 1)separate line, 2)input pop out and 3)empty line
    # minimum length per line is len_per_time, maximum length depends on index level and text

    if index_level is not None:
        left_space = index_level * left_space

    total_space = max(total_space, (len(text) + left_space + right_space))
    central_space = total_space - left_space - right_space

    if central:
        print(f'{side_border:<{left_space}s}{text:^{central_space}s}{side_border:>{right_space}s}')
    else:
        print(f'{side_border:<{left_space}s}{text:<{central_space}s}{side_border:>{right_space}s}')


def print_cmd():
    my_print("commands available:")
    for k, v in command_dict.items():
        command_line = f'{k}: {v}'
        my_print(command_line, index_level=2)
    #


def show_interface():
    print(separate_line)
    my_print("Welcome to the app", central=True)
    print(separate_line)

    print(separate_line)
    print_cmd()
    print(separate_line)

    print(separate_line)
    my_print('to execute a command, input the single character representing the command')
    print(separate_line)
    print()


def get_cmd():
    while True:
        cmd_input = input("please enter the command: ").strip().lower()

        if cmd_input not in command_dict.keys():

            if cmd_input in command_dict.values():
                print(separate_line)
                my_print('*** illegal command ***')
                my_print('to execute a command, input the single character representing the command', index_level=2)
                my_print("eg. if you want to execute \"batch renaming files\", input \"r\" only ", index_level=2)
                print(separate_line)
                continue

            print(separate_line)
            my_print('*** illegal command ***')
            print_cmd()
            my_print('to execute a command, input the single character representing the command')
            print(separate_line)
            print()
            continue
        else:
            # notice the selected cmd
            print(separate_line)
            my_print('executing command: ' + command_dict[cmd_input])
            print(separate_line)
            print()
            return cmd_input


def intention():
    # double check before executing the cmd
    txt = input('key in \"True\" to continue with current setting:').lower().strip()
    if txt == 'true':
        return True


def batch_renaming_files():

    def _loop_renaming(path, level=1, prefix=None, delimiter=' '):
        # recursion function for batch renaming
        full_dir = os.listdir(path)
        count = 1
        for name in full_dir:
            # ignore invisible files and system files
            if name.startswith(('.', '_', ',')):
                continue

            abs_name = os.path.join(path, name)

            if level == 1:
                # e.g. '3 filename'
                new_name = str(count) + delimiter + name
            else:
                # e.g. '3-1-1 filename'
                new_name = prefix + '-' + str(count) + delimiter + name

            abs_new_name = os.path.join(path, new_name)
            os.rename(abs_name, abs_new_name)
            count += 1

            if os.path.isdir(abs_new_name):
                new_prefix = new_name.split(delimiter)[0]  # ['3-1-1', 'filename'][0]
                new_level = level + 1
                _loop_renaming(path=abs_new_name, level=new_level, prefix=new_prefix)

    abs_path = get_wd()
    # see get_wd()
    if abs_path == 'x':
        return
    else:
        _loop_renaming(path=abs_path)
        end_of_cmd('r')


def de_renaming_files():
    # remove the prefix of all the files and directory under the path that user provided
    # encourage to be used only after files has been systematically renamed using cmd 'r'

    def _loop_de_renaming(path, delimiter=' '):
        # recursion function for de-renaming
        full_dir = os.listdir(path)
        for name in full_dir:
            # ignore invisible files and system files
            if name.startswith(('.', '_', ',')):
                continue

            abs_name = os.path.join(path, name)
            abs_new_name = os.path.join(path, name.split(delimiter, maxsplit=1)[-1])    # ['3-1-1', 'filename'][-1]
            os.rename(abs_name, abs_new_name)

            if os.path.isdir(abs_new_name):
                _loop_de_renaming(path=abs_new_name)
        #

    abs_path = get_wd()
    # see get_wd()
    if abs_path == 'x':
        return
    else:
        _loop_de_renaming(abs_path)
        end_of_cmd('d')


def mask_files():
    global mask_file_dict

    # file name desensitization
    def _loop_mask_files(path):
        # recursion function
        full_dir = os.listdir(path)
        for name in full_dir:

            if name.startswith(('.', '_', ',')):
                continue
                # ignore invisible files and system files

            abs_name = os.path.join(path, name)

            if np.random.randint(0, 2) == 0:
                rand_name = ''.join(list(chr(i) for i in np.random.randint(65, 91, size=np.random.randint(5, 10))))
            else:
                rand_name = ''.join(list(chr(i) for i in np.random.randint(97, 123, size=np.random.randint(5, 10))))

            if os.path.isdir(abs_name):
                abs_new_name = os.path.join(path, rand_name)
                mask_file_dict[rand_name] = name
            else:
                abs_new_name = os.sep.join([path, (rand_name + '.' + name.split('.')[-1])])
                # save the extension name for files
                mask_file_dict[rand_name + '.' + name.split('.')[-1]] = name

            os.rename(abs_name, abs_new_name)

            if os.path.isdir(abs_new_name):
                _loop_mask_files(path=abs_new_name)
        #

    abs_path = get_wd()
    mask_file_dict = {}
    # see get_wd()
    if abs_path == 'x':
        return
    else:
        _loop_mask_files(abs_path)
        end_of_cmd('m')


def export_file_tree():
    """
    export file tree to an Excel file
    exported file tree is sorted based on the prefix
    exported file name is the same name of the folder that user selected
    exported file location is in the same level of the folder that user selected

    encourage to be used only after files has been systematically renamed using cmd 'r'

    e.g.
    folder selected -> /Users/jiananwang/pycharm_projects/MP0001
    exported file name -> MP0001.xlsx
    exported file path -> /Users/jiananwang/pycharm_projects
    sorted like ->
    1 xxx
    2 xxx
    2-1 xxx
    3 xxx
    """
    def _loop_export(path):
        # recursion function for exportation file tree
        full_dir = os.listdir(path)
        for name in full_dir:
            # ignore invisible files and system files
            if name.startswith(('.', '_', ',')):
                continue

            file_list.append(name)
            abs_name = os.path.join(path, name)

            if os.path.isdir(abs_name):
                _loop_export(path=abs_name)
        #

    def _indexed_file_sort(x: str):
        # 8-10-2-1 -> (8, 10, 2, 1) for each file name prefix
        ls = []
        for i in x.split(' ')[0].split('-'):
            try:
                ls.append(int(i))
            except ValueError:
                ls.append(0)
        #
        return tuple(ls)

    def _end_lines(file_name, path):
        tip_line1 = f'exported file name: {file_name}.xlsx'
        tip_line2 = f'exported file location: {path}'
        tip_line3 = f'you should be able to find the file beside your selected folder'
        tip_lines = (tip_line1, tip_line2, tip_line3)
        return tip_lines

    abs_path = get_wd()
    # see get_wd()
    if abs_path == 'x':
        return
    else:
        file_list = []
        directory_name = abs_path.split(os.sep)[-1]
        _loop_export(path=abs_path)
        file_list.sort(key=_indexed_file_sort)
        ser = pd.Series(file_list, name=directory_name, dtype=str)
        # /Users/jiananwang/pycharm_projects/MP0001 -> MP0001
        # MP0001 will be both the column name of the series and the exported Excel file name.
        export_path = os.sep.join(list(abs_path.split(os.sep)[:-1]))
        # /Users/jiananwang/pycharm_projects/MP0001 -> /Users/jiananwang/pycharm_projects
        # the exported Excel file will appear nearby the directory
        ser.to_excel(f'{export_path}{os.sep}{directory_name}.xlsx', index=False)

        lines = _end_lines(directory_name, export_path)
        end_of_cmd('e', *lines)


def get_wd():
    # return an absolut path for a folder
    # can determine if the path exist, if the path is a folder
    # user can exist by input x
    # provide a simple view to help user to check if it is the target folder
    # only return the path after user's double check
    while True:
        wd = input('input the absolute path of the directory: \n'
                   '(input "x" to go back to main menu) \n'
                   '(input "help" to find out how to get absolute path)')

        if wd.strip().lower() == 'x':
            # when get_wd() get an x it will immediately return x to abs_path variable in the caller cmd
            # when abs_path get an x, the caller function will return none and back to main() and
            # wait for next cmd (a new while loop for main())
            print()
            return wd

        if wd.strip().lower() == 'help':
            print(separate_line)
            my_print('tips to get absolut path:')
            my_print('for MacOS users:', index_level=2)
            my_print('step1: single click the folder you want to rename', index_level=3)
            my_print('step2: press command + option + C', index_level=3)
            my_print('step3: in the input line, press command + V', index_level=3)
            my_print('for Windows users:', index_level=2)
            my_print('step1: single click the folder you want to rename', index_level=3)
            my_print('step2: press Ctrl + Shift + C', index_level=3)
            my_print('step3: in the input line, press Ctrl + V', index_level=3)
            my_print()
            my_print('absolut path example:')
            my_print('for MacOS users:', index_level=2)
            my_print('/Users/jiananwang/pycharm_projects/MP0001', index_level=3)
            print(separate_line)
            print()
            continue

        if os.path.exists(wd) is False:
            print(separate_line)
            my_print('*** illegal absolute path ***')
            my_print(f"absolute path \"{wd}\" does not exist")
            my_print(f"please try a new one")
            print(separate_line)
            print()
            continue

        if os.path.isdir(wd) is False:
            print(separate_line)
            my_print('*** illegal absolute path ***')
            my_print(f"absolute path \"{wd}\" is not a directory")
            my_print(f"please try a new one")
            print(separate_line)
            print()
            continue

        # show first level files and directories within the folder to assist double check
        print(separate_line)
        my_print(f'files(folders) within \"{wd}\" are: ')
        for i in sorted(os.listdir(wd)):
            if i.startswith(('.', '_', ',')):
                continue
            my_print(i, index_level=2)
        print(separate_line)
        print()

        # double check
        if intention():
            print(separate_line)
            my_print('path accepted')
            print(separate_line)
            print()
            return wd
        else:
            print(separate_line)
            my_print('path denied by user, please input a new one')
            print(separate_line)
            print()
    #


def end_of_cmd(command_code, *notes):
    print(separate_line)

    if command_code == 'x':
        my_print('app exited, thank you for using!')
        print(separate_line)
        return

    my_print(f'command {command_dict[command_code]} successfully executed')

    if len(notes) > 0:
        my_print()
        for i in notes:
            my_print(i)
        my_print()

    my_print(f'returning to main menu')
    print(separate_line)
    print()

    # time.sleep(3)


def main():
    while True:
        show_interface()
        cmd = get_cmd()
        if cmd == 'x':
            end_of_cmd('x')
            break
        elif cmd == 'r':
            batch_renaming_files()
        elif cmd == 'e':
            export_file_tree()
        elif cmd == 'd':
            de_renaming_files()
        elif cmd == 'm':
            mask_files()


if __name__ == '__main__':
    main()

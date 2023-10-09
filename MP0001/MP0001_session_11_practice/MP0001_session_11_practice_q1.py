#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/2 10:13
@user: jiananwang
@title: MP0001_session_11_practice_q1
"""


def inputInteger(prompt, min=0, max=999999,
                 errmsg=None,
                 exitmsg=None, exitdefault=0):
    """Obtains an integer from user."""
    while True:
        inp = input(prompt)
        inp = inp.strip()

        if exitmsg is not None:
            if inp == exitmsg:
                return exitdefault

        ## Convert to integer, like in  int(inp)
        tot = 0
        ninp  = len(inp)

        for i, c in enumerate(inp):
            # Break at the first sign of non-digit
            if c.isdigit() == False:
                if errmsg is not None:
                    print(errmsg)
                i = 0  ## a small hack to trick i<(ninp-1) to continue
                break
            ## From here on, c is a digit, but of str type
            tot = 10 * tot + (ord(c) - 48)
        #

        if i < (ninp - 1):
            continue

        ### is tot in range?
        if not (min <= tot <= max):
            if errmsg is not None:    print(errmsg)
            continue
        # tot is integer and in range
        break
        #
    return tot

v = inputInteger("Enter starting balance (press x to exit):",
                     errmsg="Sorry, wrong input; please re-enter.",
                     exitmsg="X", exitdefault=-1,
                     min=0, max=100)
if v == -1:
    print("User exited without input.")
else:
    print(f"User input value is {v}.")
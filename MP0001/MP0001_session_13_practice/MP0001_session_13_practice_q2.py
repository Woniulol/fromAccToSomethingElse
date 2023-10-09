#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/10 14:49
@user: jiananwang
@title: MP0001_session_13_practice_q2
"""

import pandas as pd

df1 = pd.DataFrame([f'{i}8' if col % 2 == 0 else f'{i}3'
                    for i in [row if row % 2 == 0 else 2 * row for row in range(5)]]
                   for col in range(8)).T
print(df1)
print(df1.shape)


df2 = pd.DataFrame([[f'{row}{i}' if row % 2 == 0 else f'{row * 2}{i}'
                     for i in [8 if col % 2 == 0 else 3 for col in range(8)]]
                    for row in range(5)])
print(df2)
print(df2.shape)

df3 = pd.DataFrame([[(i if i % 2 == 0 else i*2) * 10 + (8 if j % 2 == 0 else 3)
                     for j in range(8)]
                    for i in range(5)])
print(df3)
print(df3.shape)
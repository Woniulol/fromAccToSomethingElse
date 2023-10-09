#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/10 14:43
@user: jiananwang
@title: MP0001_session_13_practice_q1
"""


import pandas as pd

df = pd.DataFrame([[i] * 4 for i in range(1, 6+1)])

print(df)
print(df.shape)


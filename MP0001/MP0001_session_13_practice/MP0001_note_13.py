#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/10 11:00
@user: jiananwang
@title: MP0001_note_13
"""

import numpy as np
import pandas as pd
import random as rn

df1 = pd.DataFrame({
    "B": [3, 1, 6, 9],
    "D": [2, 7, 8, 9]
})

df2 = pd.DataFrame({
    "C": [7, 2, 0],
    "D": [2, 8, 0]
})

df3o_c = pd.concat([df1, df2])
df3i_c = pd.concat([df1, df2], join='inner')
df4o_c = pd.concat([df1, df2], axis=1)
df4i_c = pd.concat([df1, df2], axis=1, join='inner')

df3i_m = df1.merge(df2, left_on='D', right_on='C', how='inner')
df3o_m = df1.merge(df2, left_on='D', right_on='C', how='outer')
df4i_m = df1.merge(df2, on='D', how='inner')
df4o_m = df1.merge(df2, on='D', how='outer')

df3o_j = df1.join(df2, lsuffix='_L', rsuffix='_R', how='outer')
df3i_j = df1.join(df2, lsuffix='_L', rsuffix='_R', how='inner')

df1k = df1.set_index("D")
df2k = df2.set_index("D")
df3ko_j = df1k.join(df2k, how='outer')
df3ki_j = df1k.join(df2k, how='inner')

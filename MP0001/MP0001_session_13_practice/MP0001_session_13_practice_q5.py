#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/10 15:46
@user: jiananwang
@title: MP0001_session_13_practice_q5
"""

import pandas as pd
import numpy as np


def df_create(num_rows, num_cols, value):
    if np.isnan(value):
        df = pd.DataFrame(np.arange(1, num_rows * num_cols + 1).reshape(num_rows, num_cols))
    else:
        df = pd.DataFrame(np.full((num_rows, num_cols), value), dtype=float)
    return df


df = df_create(10, 6, np.nan)
df.columns = list("ABABAB")
df2 = pd.DataFrame({
    "AA": df.A.sum(axis=1),
    "BB": df.B.sum(axis=1)})
print(df2)

df = df_create(12, 3, np.nan)
df.columns = ["A1", "B2", "C3"]
df.index = np.arange(12)
df2 = pd.DataFrame([df.loc[df.index % 2 == 0].sum(),
                    df.loc[df.index % 2 != 0].sum()])
print(df2)

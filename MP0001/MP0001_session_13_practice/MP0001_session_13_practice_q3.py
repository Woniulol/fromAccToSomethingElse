#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/10 15:23
@user: jiananwang
@title: MP0001_session_13_practice_q3
"""

import pandas as pd
import numpy as np


def df_create(num_rows, num_cols, value):
    if np.isnan(value):
        df = pd.DataFrame(np.arange(1, num_rows * num_cols + 1).reshape(num_rows, num_cols))
    else:
        df = pd.DataFrame(np.full((num_rows, num_cols), value), dtype=float)
    return df


print(df_create(3, 5, np.nan))
print(df_create(3, 5, 10))
print(df_create(6, 5, float('nan')))

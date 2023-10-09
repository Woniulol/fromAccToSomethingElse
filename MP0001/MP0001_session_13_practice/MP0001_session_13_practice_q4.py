#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/10 15:39
@user: jiananwang
@title: MP0001_session_13_practice_q4
"""

import pandas as pd
import numpy as np


def row_create(n, value):
    if np.isnan(value):
        df = pd.DataFrame(np.arange(1, n+1), dtype=float).T
    else:
        df = pd.DataFrame([value] * n, dtype=float).T
    return df


def col_create(n, value):
    if np.isnan(value):
        df = pd.DataFrame(np.arange(1, n+1), dtype=float)
    else:
        df = pd.DataFrame([value] * n, dtype=float)
    return df


print(row_create(10, 10))
print(col_create(10, 10))
print(row_create(10, np.nan))
print(col_create(10, np.nan))


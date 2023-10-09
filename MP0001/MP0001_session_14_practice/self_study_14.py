#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/12 12:22
@user: jiananwang
@title: self_study_14
"""

import pandas as pd
import numpy as np

df6 = pd.DataFrame({
    "A": [1, 1, 1, 2, 2, 2, 3],
    "B": [3, 7, 3, 4, 5, 1, 9],
    "C": [6, 3, 4, 6, 4, 2, 3],
    "D": [8, 5, 1, 0, 0, 3, 7]
})

ss6_B = df6.B
ss6_map = ss6_B.map(lambda x: 10 - x)

df3 = pd.DataFrame({
    "A": [8, 9],
    "B": [3, 1],
    "C": [9, 0],
    "D": [9, 7]
})

df3_colprop = df3.apply(
    lambda colvec: colvec / sum(colvec))

df3_rowprop = df3.apply(
    lambda colvec: colvec / sum(colvec),
    axis=1)

df3_am = df3.applymap(
    lambda x: 2 * x
)
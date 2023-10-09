#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/24 12:03
@user: jiananwang
@title: MP0001_session_17_practice_q1
"""
import pandas as pd

file_name = 'population-un.csv'
df = pd.read_csv(file_name)
excel_file_name = 'population-un.xlsx'
df.to_excel(excel_file_name, index=False)
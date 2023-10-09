#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/24 12:09
@user: jiananwang
@title: MP0001_session_17_practice_q2
"""

import pandas as pd

# q1
file_name = 'population-un.csv'
df = pd.read_csv(file_name)

# q2
unique_location = len(df.Location.unique())
unique_year = len(df.Time.unique())

# q3
for i in ['India', 'Viet Nam']:
    location_df = df[df.Location == i]
    print(location_df)
    location_df = location_df[(location_df.Time <= 2024) & (location_df.Time >= 2018)]
    avg_pop = location_df.PopTotal.mean()
    print(f'the average population for {i} during 2018 and 2024 is: {avg_pop:,.2f}K')

# q4
df_2019_2025 = df[(df.Time >= 2019) & (df.Time <= 2025)]
locations = df_2019_2025.Location[(df_2019_2025.PopFemale / df_2019_2025.PopMale) >= 1.1]
location = locations.unique()
print(location)
print(len(location))

# q5
pop_2022 = df.loc[:, ['Location', 'PopTotal', 'PopDensity', 'Time']][df.Time == 2022]
count = 0
for i in df.Location.unique():
    df_temp = pop_2022[pop_2022.Location == i]
    index_to_save = df_temp[df_temp.PopDensity == df_temp.PopDensity.max()].index[0]
    index_to_drop = df_temp.index[df_temp.index != index_to_save]
    pop_2022 = pop_2022.drop(index=index_to_drop)
    count += 1
#
pop_2022_sorted = pop_2022.sort_values(by=['PopDensity'], ascending=False)
pop_2022_sorted.to_html('pop_2022_sorted.html')

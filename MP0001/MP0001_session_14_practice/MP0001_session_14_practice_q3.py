#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/7/12 14:25
@user: jiananwang
@title: MP0001_session_14_practice_q3
"""

import pandas as pd


def total_population_year(df, year):
    return df.T.loc['Total Population (year-end)(10000 persons)', str(year)]


population_data = pd.read_csv('population-cn_class.csv',
                              index_col="Indicators").T
year = 2016
print(f'{"="*10} Q3a {"="*10}')
print(f'total population in year {year}: {total_population_year(population_data, 2016)}')

female_population_year_beginning = population_data['Female Population(10000 persons)'][1:]
female_population_year_end = population_data['Female Population(10000 persons)'][:-1]
female_population_year_beginning.index = female_population_year_end.index

female_population_difference = female_population_year_end - female_population_year_beginning
print(f'{"="*10} Q3b {"="*10}')
print(f'year female population first start declining: '
      f'{female_population_difference[female_population_difference < 0].index.min()}')

female_male_difference = population_data["Male Population(10000 persons)"] \
                         - population_data["Female Population(10000 persons)"]
min_difference = female_male_difference.min()
max_difference = female_male_difference.max()
print(f'{"="*10} Q3c {"="*10}')
print(f'year the difference between male and female population is the smallest: '
      f'{female_male_difference[female_male_difference == min_difference].index[0]}')
print(f'year the difference between male and female population is the largest: '
      f'{female_male_difference[female_male_difference == max_difference].index[0]}')

population_data['MaleFemaleRatio'] = round(population_data['Male Population(10000 persons)']
                                           / population_data['Female Population(10000 persons)'], 4)
male_female_ratio_min = population_data['MaleFemaleRatio'].min()
male_female_ratio_max = population_data['MaleFemaleRatio'].max()
print(f'{"="*10} Q3d {"="*10}')
print(f"min male and female ratio: {population_data[population_data['MaleFemaleRatio'] == male_female_ratio_min].index[0], male_female_ratio_min}")
print(f"max male and female ratio: {population_data[population_data['MaleFemaleRatio'] == male_female_ratio_max].index[0], male_female_ratio_max}")
print(f'male and female ratio in 2020: {population_data.loc["2020", "MaleFemaleRatio"]}')

population_data['DiffUrbRur'] = population_data['Urban Population(10000 persons)'] \
                                - population_data['Rural Population(10000 persons)']
urban_rural_difference_year_beginning = population_data['DiffUrbRur'][1:]
urban_rural_difference_year_end = population_data['DiffUrbRur'][:-1]
urban_rural_difference_year_beginning.index = urban_rural_difference_year_end.index
urban_rural_difference_growth_rate = (urban_rural_difference_year_end / urban_rural_difference_year_beginning - 1) * 100

urban_rural_difference_growth_rate_min = urban_rural_difference_growth_rate.min()
urban_rural_difference_growth_rate_max = urban_rural_difference_growth_rate.max()
urban_rural_difference_growth_rate_average = urban_rural_difference_growth_rate.mean()
print(f'{"="*10} Q3e {"="*10}')
print(urban_rural_difference_growth_rate[urban_rural_difference_growth_rate == urban_rural_difference_growth_rate_min].index[0])
print(urban_rural_difference_growth_rate[urban_rural_difference_growth_rate == urban_rural_difference_growth_rate_max].index[0])
print(urban_rural_difference_growth_rate_average)






#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@user: jiananwang
@title: WANG JIANAN CBA_para_select_cart.py
"""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import tqdm
import random


df = pd.read_csv('/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6006 Course Materials/AY23 CBA/marun_sample2.csv')

df.dropna(axis=0, inplace=True)  # drop NA rows

df.columns = ["Northing", "Easting", "DepthFT", "Formation", "PorePressure", "FracturePressure", "MudPressurePSI", "HoleSizeIN", "METERAGE", "DRLTIME", "WOB", "PumpFlowRate", "PumpPressure", "MFVIS", "RETSOLID", "FAN600", "FAN300", "MIN10GEL", "RPM", "MUDLOSSU"]

# transfer to categorical
for i in ['Formation', 'HoleSizeIN']:
    df[i] = df[i].astype(str)

categories_Formation = [[str(i) for i in range(1,16)]]  # set categories 

my_ls = [float(i) for i in list(df['HoleSizeIN'].value_counts().index)]
categories_HoleSizeIN = [[str(i) for i in sorted(my_ls)]]  # sort to ensure the one level dorp is the base level

OneHotEncoder_Formation = OneHotEncoder(categories=categories_Formation, drop='first')  # drop the first level, matching R's treatment to categorical variable
OneHotEncoder_HoleSizeIN = OneHotEncoder(categories=categories_HoleSizeIN, drop='first')  # drop the first level, matching R's treatment to categorical variable

preprocessor = ColumnTransformer(
    transformers = [
        ('oeF', OneHotEncoder_Formation, ['Formation']),
        ('oeH', OneHotEncoder_HoleSizeIN, ['HoleSizeIN'])
    ],
    remainder='passthrough'
)

df_preprocessed = pd.DataFrame(preprocessor.fit_transform(df))  # encode the data

df_preprocessed.columns = ['Formation'+ i for i in categories_Formation[0]][1:] + ['HoleSizeIN' + i for i in categories_HoleSizeIN[0]][1:] + ["Northing", "Easting", "DepthFT", "PorePressure", "FracturePressure", "MudPressurePSI", "METERAGE", "DRLTIME", "WOB", "PumpFlowRate", "PumpPressure", "MFVIS", "RETSOLID", "FAN600", "FAN300", "MIN10GEL", "RPM", "MUDLOSSU"]
print(df_preprocessed)
print(df_preprocessed.columns)

X = df.drop(columns='MUDLOSSU')
Y = df['MUDLOSSU']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=6006)

my_param_grid = {
    'criterion': ['squared_error'],  
# measure the split quality
    'max_depth': [i for i in range(1, 10)],       
# The maximum depth of the tree. Prune result in R indicates there is no need a very high depth
    'min_samples_split': [i for i in range(2, 300, 3)],                
# The minimum number of samples required to split an internal node
    "min_samples_leaf": [i for i in range(1, 300, 3)]
# The minium number of samples required in a terminal node
}

grid_search = GridSearchCV( DecisionTreeRegressor(), param_grid=my_param_grid, 
                           cv = 10, scoring='neg_mean_squared_error',
                           verbose=2, n_jobs=-1 )  # try to match default setting of R

grid_search.fit(X_train, Y_train)

best_params = grid_search.best_params_
print(best_params)

# {'criterion': 'squared_error', 'max_depth': 6, 'min_samples_leaf': 7, 'min_samples_split': 38}

# # model = DecisionTreeRegressor(min_samples_leaf=7, min_samples_split=38, max_depth=6, random_state=6006)
# # model.fit(X_train, Y_train)
# # rmse = mean_squared_error(Y_test, model.predict(X_test)) ** 0.5
# # print(rmse)

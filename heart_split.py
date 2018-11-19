# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:57:21 2018

@author: james
"""


import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

feature_names_ht = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
class_names_ht = ["NoDisea", "Disease"]

df = pd.read_csv("heart.csv")





train, test = train_test_split(df, test_size=0.2)
train.to_csv("heart_train.csv", header=None, index=None)
test.to_csv("heart_test.csv", header=None, index=None)




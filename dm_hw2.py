# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:57:21 2018

@author: james
"""

from sklearn import tree
import graphviz
import numpy as np
import pandas as pd
from sklearn import preprocessing

feature_names_sw = ["days", "temp", "milk", "veg", "meat", "price", "poison", "clean", "sex", "smoke", "cust"]
class_names_sw = ["Rotten", "Edible"]
feature_names_ht = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
class_names_ht = ["NoDisea", "Disease"]
feature_names_bk = ["age", "job", "marital", "education", "default", "balance", "housing", "loan", "contact", "day", "month", "duration", "campaign", "pdays", "previous", "poutcome"]
class_names_bk = ["no", "yes"]
#df = pd.read_csv("sandwich_data.csv", header=None)
#df_test = pd.read_csv("sandwich_test.csv", header=None)
#df = pd.read_csv("sandwich_data_easy.csv", header=None)
#df_test = pd.read_csv("sandwich_test_easy.csv", header=None)
#df = pd.read_csv("heart_train.csv", header=None)
#df_test = pd.read_csv("heart_test.csv", header=None)
df = pd.read_csv("bank-full.csv")
df_test = pd.read_csv("bank.csv")
#%%
#preprocessing (category to numeric)

le = preprocessing.LabelEncoder()


for w in df.columns.values:
    #if w != ("age" or "balance" or "day" or "duration" or "campaign" or "pdays" or "previous" ):
        df[w] = le.fit_transform(df[w])

for w in df_test.columns.values:
    #if w != ("age" or "balance" or "day" or "duration" or "campaign" or "pdays" or "previous" ):
        df_test[w] = le.fit_transform(df_test[w])

#%%
X = []
test_X = []
test_Y = []
tmp = []
prune_perc = 0.02
for i in range(len(df)):
    tmp = df.iloc[i,0:len(df.iloc[0,:])-1].tolist()
    X.append(tmp)
    
for i in range(len(df_test)):
    tmp = df_test.iloc[i,0:len(df_test.iloc[0,:])-1].tolist()
    test_X.append(tmp)
    
Y = df.iloc[:,len(df.iloc[0,:])-1].tolist()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

#%%
#pruning??
#
from sklearn.tree._tree import TREE_LEAF

def prune_index(inner_tree, index, threshold):
    if inner_tree.value[index].min() < threshold:
        # turn node into a leaf by "unlinking" its children
        inner_tree.children_left[index] = TREE_LEAF
        inner_tree.children_right[index] = TREE_LEAF
    # if there are shildren, visit them as well
    if inner_tree.children_left[index] != TREE_LEAF:
        prune_index(inner_tree, inner_tree.children_left[index], threshold)
        prune_index(inner_tree, inner_tree.children_right[index], threshold)

#print(sum(dt.tree_.children_left < 0))
# start pruning from the root
prune_index(clf.tree_, 0, int(prune_perc * len(df)))
#%%
#dot_data = tree.export_graphviz(clf, out_file=None, 
#                         feature_names=feature_names_bk,  
#                         class_names=class_names_bk)  

test_y_predicted = clf.predict(test_X)
#print(test_y_predicted)
#graph = graphviz.Source(dot_data)
#graph.render("Real Bank Tree preprocess 0.2%", view=True) 

#%%
#Evaluate result (for prunung)
count = 0
for i in range(len(df_test)):
    if df_test.iloc[i,len(df_test.iloc[0,:])-1] != test_y_predicted[i]:
        count = count + 1


print("ACC: " , (len(df_test)-count)/len(df_test))

#%%
from sklearn import metrics
#predict_prob_y = clf.predict_proba(test_X)#基于SVM对验证集做出预测，prodict_prob_y 为预测的概率
#end svm ,start metrics 
test_Y = df_test.iloc[:,len(df_test.iloc[0,:])-1].tolist()
test_auc = metrics.roc_auc_score(test_Y, test_y_predicted)#验证集上的auc值
print("AUC: ", test_auc)
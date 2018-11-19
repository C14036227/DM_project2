# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:09:01 2018

@author: james
"""



import numpy as np
import pandas as pd 
import random as rd


#rule based
def genlabel(atr):
    #day: 0
    #temp: 1
    #milk: 2
    #veg: 3
    #meat: 4
    #price: 5
    #poison: 6
    #clean: 7
    #sex: 8
    #smoke: 9
    #cust: 10
    label = 1
    
    if atr[0]>3:
        label = 0
    elif atr[1]>28:
        label = 0
    elif atr[6]==1:
        label = 0
#    elif atr[0]>1.5 and atr[2]==1:
#        label = 0
#    elif atr[0]>2 and atr[3]==1:
#        label = 0
#    elif atr[0]>2.5 and atr[4]==1:
#        label = 0
#    elif atr[5]<20 and atr[2]==1:
#        label = 0
    elif atr[5]<15:
        label = 0
    elif atr[7]==4:
        label = 0
#    elif atr[7]==3 and atr[0]>1 and atr[1]>26 and atr[5]<25:
#        label = 0
#    elif atr[7]==2 and atr[0]>2 and atr[1]>25 and atr[5]<25:
#        label = 0
#    elif atr[8]==1 and (atr[7]==3 or atr[7]==4):
#        label = 0
    elif atr[9]==1: #and atr[0]>2:
        label = 0
#    elif atr[7]==3 and atr[10]==2:
#        label = 0
#    elif atr[9]==1 and atr[5]<25:
#        label = 0
    atr.append(label)
    return atr










if __name__=="__main__":
    attrib = []
    label = []
    test = []
    datalen = 2000
    
    for i in range(datalen):
        #gendata
        rowdata = []
        temp = round(rd.uniform(16,32),2)
        days = round(rd.uniform(0,4), 1)
        milk = rd.uniform(0,1)
        if milk >0.8:
            milk=1
        else:
            milk=0
        veg = rd.randint(0,1)
        meat = rd.randint(0,1)
        poison = rd.uniform(0,1)
        if poison>0.8:
            poison = 1
        else:
            poison = 0
        price = rd.randint(5,55)
        clean = rd.randint(0,4)
        sex = rd.randint(0,1)
        smoke = rd.uniform(0,1)
        if smoke>0.8:
            smoke = 1
        else:
            smoke = 0
        cust = rd.randint(0,2)
        rowdata = [days, temp, milk, veg, meat, price, poison, clean, sex, smoke, cust]
        rowdata = genlabel(rowdata)
        attrib.append(rowdata)
        
    for i in range(500):
        #gendata
        rowdata = []
        temp = round(rd.uniform(16,32),2)
        days = round(rd.uniform(0,4), 1)
        milk = rd.uniform(0,1)
        if milk >0.8:
            milk=1
        else:
            milk=0
        veg = rd.randint(0,1)
        meat = rd.randint(0,1)
        poison = rd.uniform(0,1)
        if poison>0.8:
            poison = 1
        else:
            poison = 0
        price = rd.randint(5,55)
        clean = rd.randint(0,4)
        sex = rd.randint(0,1)
        smoke = rd.uniform(0,1)
        if smoke>0.8:
            smoke = 1
        else:
            smoke = 0
        cust = rd.randint(0,2)
        rowdata = [days, temp, milk, veg, meat, price, poison, clean, sex, smoke, cust]
        rowdata = genlabel(rowdata)
        test.append(rowdata)
        
    df = pd.DataFrame(attrib)
    df_test = pd.DataFrame(test)
    df.to_csv("sandwich_data_easy.csv", header=None, index=None)
    df_test.to_csv("sandwich_test_easy.csv", header=None, index=None)
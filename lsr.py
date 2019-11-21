#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:58:45 2019

@author: koshal
"""
import pandas as pd
import numpy as np

#c1
def LeastSquare(X,Y):
    n = len(X)
    sum_x=sum(X)
    sum_y=sum(Y)
    nxy=sum(n*[X[i]*Y[i] for i in range(n)])
    Sum_X_Y = sum_x*sum_y
    n_x2=n*sum([X[i]**2 for i in range(n)])
    x2=sum(X)**2
    C1=(nxy-Sum_X_Y)/(n_x2-x2)    
    C0=(sum_y-c1*sum_x)/n
    E0=[Y[i]-c0-c1*X[i] for i in range(n)]
    E=sum([E0[i]**2 for i in range(len(E0))])
    return C1,C0, E

#driver program
# Preprocessing Input data
data = pd.read_csv('data.csv')

X = data.iloc[:70, 0]#training data X
Y = data.iloc[:70, 1]#training data y
#print(X,Y)
X1 = data.iloc[71:98, 0]
Y1 = data.iloc[71:98, 1]
x1=np.array(X1)
Y1=np.array(Y1)
c1, c0, e= LeastSquare(X,Y) #c1 c0 obtained from training data
for i in range(len(X1)):
    print(X1[i])
#Test_Y=[c1*X1[i]+c0+e for i in range(len(X1))]
#print('test y:  ',Test_Y)
print(Y1)
print(X1)
#for i in range(len(X1)):
#    print(i, '    ', Test_Y[i],'    ', Y1[i])
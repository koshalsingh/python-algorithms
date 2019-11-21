#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:00:55 2019

@author: curaj
"""
import numpy as np
#power iteration 
def powerIteration(A, X0):
    for i in range(10):
        X1=np.dot(A, X0)
        lamda = np.amax(X1)
        print(X1)
        X1=X1/lamda
        print(X1)
        print(i)
        if(X1==X0):
            break
        X0=X1
    
    return X1

#driver program
a=[[2,-12],[1,-5]]
x=[1,1]
e=list(powerIteration(a,x))
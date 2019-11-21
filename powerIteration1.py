#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:51:49 2019

@author: curaj
"""
import numpy as np

def powerIteration(a, x):
    for i in range(100):
    x1=np.dot(a,x)
    h=0
    if(x1[0]>x1[1]):
       h=x1[1]
    if(x1[0]<x1[1]):
       h=x1[0]         
    
    x1[0]=x1[0]/h
    x1[1]=x1[1]/h
    print(h)
    if(abs(x1[0]-x[0])<1 and abs(x1[1]-x[1])<1):
        return x1,h
    else:
        powerIteration(a,x1)
#driver program
a=[[2,-12],[1,-5]]
x=[1,1]
e=list(powerIteration(a,x))
value=e[1]
vector=e[0]
print('eigen value = ',value, ' eigen vector = ',vector)
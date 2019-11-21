#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:44:58 2019
                            POWER ITERATION
@author: koshal
"""
import numpy as np

#Eigen value
def eigenValue(A,x):
    Ax=np.dot(A,x)
    xt=np.transpose(x)
    xtx=np.dot(x,xt)
    value = (np.dot(Ax,xt))/xtx
    print(value)
    return value

#norming the vector
def norm(X):
    X=[abs(i) for i in X]
    lamda = min(X)
    print('min=',lamda)
    X=[i/lamda for i in X]
    X=np.concatenate((X[0], X[1]))
    #print(X)
    return X               
        
#power iteration 
def powerIteration(A, X0):
    for i in range(10):
        X1=np.dot(A, X0)
        lamda = np.amin(X1)
        X1=X1/lamda        
        if(np.allclose(norm(X1),norm(X0))):
            break
        X0=X1
    
    return X1, lamda


#driver program
A= np.array([[2,-12],[1,-5]])
x= np.array([[1],[1]])

e=list(powerIteration(A,x))

print('eigen value: ', eigenValue(A,e[0]))
print('eigen vector: ', e[0])

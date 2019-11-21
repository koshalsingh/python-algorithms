#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:31:19 2019

@author: curaj
"""
import numpy as np
def GaussSeidel(A,x,b,T,C):
    x1 = [0,0]
    i = 0
    while(i<=10):
        x1 = np.add(np.dot(T,x),C)
        x = x1
        i = i+1
    print(x1)
    
A = np.array([[16,3],[7,-11]])
U = np.array([[0]*2]*2)
L = np.array([[0]*2]*2)

for i in range(2):
    for j in range(2):
        if(i<j):
            
            U[i,j] = A[i,j]
        if(i>=j):
            
            L[i,j] = A[i,j]

b = np.array([11,13])

x = np.array([1,1])

T = np.dot(-(np.linalg.inv(L)),U)
C = np.dot(np.linalg.inv(L),b)

b = np.shape(np.matrix([11,13]))

x = np.array([1,1])
GaussSeidel(A,x,b,T,C)
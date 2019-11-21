#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:44:24 2019

@author: curaj
"""

import numpy as np

#lower matrix
def lower(a):
    n=np.shape(a)[0]
    m=np.shape(a)[1]
    l=np.zeros([2,2], dtype='int')
    for i in range(n):
        for j in range(m):
            if(i>=j):            
                l[i][j]=a[i][j]
    return l

#upper matrix
def upper(a):
    n=np.shape(a)[0]
    m=np.shape(a)[1]
    u=np.zeros([2,2], dtype='int')
    for i in range(n):
        for j in range(m):            
            if(i<j):
                u[i][j]=a[i][j]
    return u

#gauss Seidel function to do main task
def GaussSeidel(a,b):
    #the lower matrix with zeroes in upper half
    l=lower(a)
    print(l)
    #the upper matrix with zeroes in lower half
    u=upper(a)
    print(u)
    #inversing the matrix l 
    l=np.linalg.inv(l)
    print(l) 
    t=-1*np.dot(l,u)
    c=np.dot(l,b)
    print(t,c)
    x=[1,1]
    
    x=np.dot(t,x)+c
    print(x)
#driver program
#creating matrix a using np
a=np.array([[16,3],[7,-11]])
print(a)
#creating matrix b(the results)
b=np.array([[11],[13]])

GaussSeidel(a,b)
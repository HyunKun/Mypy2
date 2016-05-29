# -*- coding: utf-8 -*-
"""
Created on Fri May 27 17:31:50 2016

@author: 현건
"""
from Sets import *

class dfield:
    def __init__(self,L):
        self.elements = L

class dprobability:
    def __init__(self,dfield,distribution):
        self.field = dfield
        self.dist = distribution
        self.omega = (self.field).elements
    def sprob(self,a):
        ai =  isin(a,self.omega)[1]
        return self.dist[ai]
    def mprob(self,A):
        S = 0
        for elem in A:
            S+= self.sprob(elem)
        return S
    def prob(self, A ,B = []):
        if B != []:
            return (self.mprob(A|n_|B))/(self.mprob(B))
        else:
            return self.mprob(A)
        
    def inde(self,A,B):
        if self.prob(A|n_|B) == (self.prob(A))*(self.prob(B)):
            return 1
        else:
            return 0
            

class singleTon:
    def __init__(self,count =0):
        self.count = count
    def hit(self,n=1):
        self.count += n
    
def exp2prob(*singles):
    N = 0
    L = []
    dist = []
    for x in singles:
        L +=[x]
        N += x.count
    df = dfield(L)
    for x in singles:
        if N>0:          
            dist += [x.count/N]
        else:
            dist +=[x.count]
    return dprobability(df,dist)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
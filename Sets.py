# -*- coding: utf-8 -*-
"""
Created on Thu May 26 18:16:14 2016

@author: 현건
"""
import sympy
import numpy as np


#############################################################
class Infix:
    "http://code.activestate.com/recipes/384122/"
    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return lbind(self.function, other)
    def __or__(self, other):
        return rbind(self.function, other)

class rbind:
    def __init__(self, function, binded):
        self.function = function
        self.binded = binded
    def __ror__(self, other):
        return self.function(other, self.binded)
    def __call__(self, other):
        return self.function(other, self.binded)

class lbind:
    def __init__(self, function, binded):
        self.function = function
        self.binded = binded
    def __or__(self, other):
        return self.function(self.binded, other)
    def __call__(self, other):
        return self.function(self.binded, other)

 ###########################################################

def isin(x,a):
    "Returns [val,n] val = 0 or 1 depending of whether x is an element of 'a' ,n is the index where x is but is zero if x is not in a"
    
    
    val = 0
    n = 0
    for i in range(0, len(a)):

        if x == a[i]:
            val = 1
            n = i
            break
    return [val,n]

in_ = Infix(lambda x,a: isin(x,a))



def Table(T,a,b):
    [va,na] = isin(a,T[0])
    [vb,nb] = isin(b,T[0])
    if va*vb == 1:
        return T[na][nb]


def mt(T,A):
    if len(A) ==2:
        return Table(T,A[0],A[1])
    else :
        AA = [Table(T,A[0],A[1])]+A[2:len(A)]
        return mt(T,AA)
        



def sisin(A,B):

    L = len(A)
    Lb = len(B)
    [y,n]=isin(A[0],B)
    if y == 0:
        return 0
    if L == 1:
        return 1
    else:
        AA = A[1:L]
        BB = B[0:n] + B[n+1:Lb]
        return sisin(AA,BB)
        
sin_ = Infix(lambda A,B: sisin(A,B))

def sand(A,B,S = [],count = 0):
    count +=1
    if count ==1:
        S = []
    L = len(A)
    Lb = len(B)
    [y,n]=isin(A[0],B)

    if y == 1:
        S+= [B[n]]
    if L == 1:
        return S

    else:
        AA = A[1:L]
        if y==1:
            BB = B[0:n] + B[n+1:Lb]
        else:BB = B[:]
        return sand(AA,BB,S,count)

n_ = Infix(lambda A,B: sand(A,B))
    
def msand(ListOfSets):
    if len(ListOfSets) == 1:
        return ListOfSets[0]
    if len(ListOfSets) == 2:
        return sand(ListOfSets[0],ListOfSets[1])
    else:
        return msand([sand(ListOfSets[0],ListOfSets[1])] + ListOfSets[2:len[ListOfSets]])
    
def seq(A,B):
    "This returns 1 (resp. 0) if set A is equal (resp.not equal) to set B"
    N = sand(A,B)
    if sisin(A,N):
        if sisin(B,N):
            return 1
        else:
            return 0 
    else: return 0

eq_ = Infix(lambda A,B: seq(A,B))

def Union(A,B):
    n = sand(A,B)
    Union = []
    for x in A:
        if isin(x,n)[0]==0:
            Union += [x]
    Union += B
    return Union
u_ = Infix(lambda A,B: Union(A,B))         

class dRule:
    def __init__(self,rules):
        dom = []
        img = []
        for x in rules:
            dom += [x]
            img += [rules[x]]
       
        
        self.rules = rules
        self.domain = dom
        self.image = img
    
    
class Group:
    def __init__(self,T):
        self.table = T
        self.order = len(T[0])
    
    def p(self,a,b):
        T = self.table
        return Table(T,a,b)
        
    def mulp(self,List):
        T = self.table
        return mt(T,List)
 
def Switch(A,i,j):
    aj = A[j]
    ai = A[i]
    B = A
    B[i] = aj
    B[j] = ai
    return B
       
def OrderList(L):
    N = len(L)
    A = L
    for i in range(0,N):
        [d,j]= (min(A[i:N])|in_|A)
        A = Switch(A,i,j)
    return A



#def Isomorphic(A,B,f):
#    for         
        
        
    # To define Isomorphism: First use sympt to make a symbollic copy of
    # G1's Table and G2's Table as Matrixes
    # Secondly we need a function or method to compare similarity transform
    # of the two functions
        
    

    
            
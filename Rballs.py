# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:52:10 2016

@author: 현건
"""
from Sets import *
from sympy import *

class ball: #Ball
    def __init__(self,x, dx = Rational(1,2) , Open = 0.5):
        self.x = x
        self.dx = dx
        self.ub = x+dx
        self.lb = x-dx
        self.open = Open
        
        if Open == 0 :
            self.hasu = 1
            self.hasl = 1
        elif Open == 0.5:
            self.hasu = 0
            self.hasl = 1
        elif Open == -0.5:
            self.hasu = 1
            self.hasl = 0           
        else :
            self.hasu = 0
            self.hasl = 0
            
    def show(self):
        ub=self.ub
        lb=self.lb
        Open = self.open
        if Open == 0 :
            print('[',lb,',',ub,']')
        if Open == 0.5 :
            print('[',lb,',',ub,')')
        if Open == -0.5 :
            print('(',lb,',',ub,']')
        if Open == 1 :
            print('(',lb,',',ub,')')
    def expand(self, detail = 0.01):
        x1 = self.x
        x2 = self.x
        s = detail
        L =[x1]
        smax = self.dx
        while s < smax:
            x1 += detail
            x2 -= detail
            L = [x2] + L +[x1]
            s += detail
        if s == smax:
            if self.open == 0:
                x1 += detail
                x2 -= detail
                L = [x2] + L +[x1]
            elif self.open == -0.5:
                x1 += detail
                L = L +[x1]
            elif self.open == 0.5:
                x2 -= detail
                L = [x2] + L
        return L
        
    def has(self,y):
        T = 0
        ub = self.ub
        lb = self.lb
        op = self.open
        if lb < y < ub:
            T = 1
        elif y == lb and op == 0.5:
            T = 1    
        elif y == ub and op == -0.5:
            T = 1
        return T
    def inc(self,other):
        ub = self.ub
        lb = self.lb
        oub = other.ub
        olb = other.lb
        hasu=self.hasu
        hasl=self.hasl
        ohasu=other.hasu
        ohasl=other.hasl
        if self.has(oub) and self.has(olb):
            return 1
        elif ub == oub and lb < olb and hasu >= ohasu:
            return 1
        elif lb == olb and oub < ub and hasl >= ohasl:
            return 1
        elif ub == oub and lb == olb and hasu >= ohasu and hasl >= ohasl:
            return 1
        else:
            return 0
                    
    def ins(self,other):
        return other.inc(self)


def h2o(di,si):
    if [di,si] == [0,0]:
        return 1
    if [di,si] == [1,0]:
        return 0.5
    if [di,si] == [0,1]:
        return -0.5
    if [di,si] == [1,1]:
        return 0
def o2h(o):
    if o == 0 :
        return [1,1]
    if o == 0.5 :
        return [1,0]
    if o == -0.5 :
        return [0,1]
    if o == 0 :
        return [0,0]


def superball(*balls):
    superList = []
    duperList = []
    i = 0
    for b in balls:
        if i == 0:
            Super = b.ub
            Duper = b.lb
            superList = [Super, b.hasu]
            duperList = [Duper, b.hasl]
            i +=1
        else:
            if Super < b.ub:
                Super = b.ub
                superList = [Super, b.hasu]
            if Super == b.ub:
                superList[1] = max(superList[1],b.hasu)
            if Duper == b.lb:
                duperList[1] = max(duperList[1],b.hasl)
            if Duper > b.lb:
                Duper = b.lb
                duperList = [Duper, b.hasl]
    s = superList[0]
    si = superList[1]
    d = duperList[0]
    di = duperList[1]
    x = (s+d)/2
    dx = (s-d)/2
    if [di,si] == [0,0]:
        return ball(x,dx,1)
    if [di,si] == [1,0]:
        return ball(x,dx,0.5)
    if [di,si] == [0,1]:
        return ball(x,dx,-0.5)
    if [di,si] == [1,1]:
        return ball(x,dx,0)
  
def uniball(b1,b2):
    if b1.ub < b2.lb or b1.lb > b2.ub:
        return None
    if (b1.ub == b2.lb) and (b1.hasu + b2.hasl == 0):
        return None
    if (b2.ub == b1.lb) and (b2.hasu + b1.hasl == 0):
        return None
    d = min(b1.lb,b2.lb)
    s = max(b1.ub,b2.ub)
    if b1.ub == b2.ub:
        si = max(b1.hasu,b2.hasu)
    if b1.ub > b2.ub:
        si = b1.hasu
    if b1.ub < b2.ub:
        si = b2.hasu
        
    if b1.lb == b2.lb:
        di = max(b1.hasl,b2.hasl)
    if b1.lb > b2.lb:
        di = b2.hasl
    if b1.lb < b2.lb:
        di = b1.hasl
    
    x = (s+d)/2
    dx = (s-d)/2   
    
    
    if [di,si] == [0,0]:
        return ball(x,dx,1)
    if [di,si] == [1,0]:
        return ball(x,dx,0.5)
    if [di,si] == [0,1]:
        return ball(x,dx,-0.5)
    if [di,si] == [1,1]:
        return ball(x,dx,0)

def Ordered(A):
    for i in range(0,len(A)-1):
        if A[i] > A[i+1]:
            return 0 
    return 1

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

def minx(L):
    r = oo
    mb = None
    for b in L:
        if b.x < r:
            r = b.x
            mb = b
    return mb
            


def Orderballs(L):
    N = len(L)
    A = L
    for i in range(0,N):
        [d,j]= (minx(A[i:N])|in_|A)
        A = Switch(A,i,j)
    return A

def maximal(L):
    A = Orderballs(L)
    N = len(A)
    A2 = A
    for i in range(0,N-1):
        if uniball(A[i],A[i+1]) !=None:
            A2[i] = uniball(A[i],A[i+1])
            A2 = A2[0:i+1] + A2[i+2:N]
    N = len(A2)
    if N == len(A):
        return A
    else:
        return maximal(A2)

                   
 
class Interball:
    def __init__(self,*balls):
       L = []
       for ball in balls:
           L += [ball]
       L = maximal(L)
       self.balls = L
       
    def show(self):
        for ball in self.balls:
           print(ball.show())
    def expand(self,detail = 0.01):
        L = []
        for ball in self.balls:
            L = L + ball.expand(detail)
        return L
       
def Makeb(a,b,Open =0.5):
    return ball((a+b)/2,abs(a-b)/2,Open)
            
        
                
                
                
                
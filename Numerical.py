# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:33:48 2016

@author: 현건
"""

from sympy import *
from mpmath import *
import matplotlib.pyplot as plt
from Sets import*
from Rballs import *



def simroot(f,a,b):
	"""Returns 0 or 1 for continuous f if 
	it can be proved it has a root only by 
	substituting f(a), f(b)"""
	sa = f(a)
	sb = f(b)
	if sa*sb <= 0:
		return 1
	else:
		return 0
		
# sn = lambda x: sin(x)
def simsearch(f,a = 0,N = 100,da = 1):
	A = a
	if N == 0:
		return 'Nada Take another guess'
	if simroot(f,A,A+da):
		return [A,A+da]
	else:
		A = A+da
		N -= 1
		return simsearch(f,A,N,da)

	

a = lambda x: x - 3**(-x)
b = lambda x: 4*x**2 - E**x
c = lambda x: x**3 -2*x**2 - 4*x +3
d = lambda x: x**3 +4.001*x**2 +4.002*x +1.101

print(simsearch(a))
print(simsearch(b))
print(simsearch(c))
print(simsearch(d,da = -1))
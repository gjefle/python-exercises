# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 21:27:52 2016

@author: Gjermund (actually copy pase from solutions)
"""

from numpy import linspace, zeros, sqrt, log
from integral_methods import midpoint, trapezoidal
def adaptive_integration(f, a, b, eps, method='midpoint'):
    n_limit = 1000000 # Just a choice (used to avoid inf loop)
    n = 2
    if method == 'trapezoidal':
        integral_n = trapezoidal(f, a, b, n)
        integral_2n = trapezoidal(f, a, b, 2*n)
        diff = abs(integral_2n - integral_n)
        print 'trapezoidal diff: ', diff
        while (diff > eps) and (n < n_limit):
            integral_n = trapezoidal(f, a, b, n)
            integral_2n = trapezoidal(f, a, b, 2*n)
            diff = abs(integral_2n - integral_n)
            print 'trapezoidal diff: ', diff
            n *= 2
    elif method == 'midpoint':
        integral_n = midpoint(f, a, b, n)
        integral_2n = midpoint(f, a, b, 2*n)
        diff = abs(integral_2n - integral_n)
        print 'midpoint diff: ', diff
        while (diff > eps) and (n < n_limit):
            integral_n = midpoint(f, a, b, n)
            integral_2n = midpoint(f, a, b, 2*n)
            diff = abs(integral_2n - integral_n)
            print 'midpoint diff: ', diff
            n *= 2
    else:
        print 'Error - adaptive integration called with unknown par'
# Now we check if acceptable n was found or not
    if diff <= eps: # Success
        print 'The integral computes to: ', integral_2n
        return n
    else:
        return -n # Return negative n to tell "not found"
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:11:39 2016

@author: Gjermund
"""
from integral_methods import trapezoidal, midpoint


#Chapter 3 - Exercises

#Exercise 3.1 Trapezoidal vs Hand calculations
start = 1
end = 3
f = lambda x: 2*x**3
by_hand = 40
print 'Exercise 1, 2'
print 'By hand: %g, Using trapezoidal: %g' % (by_hand, trapezoidal(f,start, end, 2))

# Exercise 3.2 Midpoint vs hand calculations
print 'Using midpoint: %g' % (midpoint(f, start, end, 2))
print ''

# Exercise 3.3 Simple integral using trapezoidal and midpoint
start = 2
end = 6
f = lambda x: x*(x-1)
n = 2
m = midpoint(f, start, end, n)
em = abs(expected - m)
t = trapezoidal(f, start, end, n)
et = abs(expected - t)
expected = 53.33333333333333
print 'Exercise 3'
print 'Using 2 intervals - Midpoint: %g (%g), trapezoidal: %g (%g)' % (m, em, t, et)
n = 100
m = midpoint(f, start, end, n)
em = abs(expected - m)
t = trapezoidal(f, start, end, n)
et = abs(expected - t)
print 'Using 100 intervals - Midpoint: %g (%g), trapezoidal: %g (%g)' % (m, em, t, et)
print ''

#Exercise 3.4
  

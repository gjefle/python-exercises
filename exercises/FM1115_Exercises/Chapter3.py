# -*- coding: utf-8 -*-
# Chapter 3 - Computing integrals

# Task 1 - Exercise from Fronter

# Trapezoidal integral method
def trapezoidal(f, a, b, n): 
    # Resolution h
    h = float(b-a)/n
    # Calculate first and last values
    sum = 0.5*(f(a) + f(b))
    
    # Iterate over values. 
    # First (a) and last value (b) is skipped.
    for i in range(1, n):
        sum +=  f(a + i*h)
    sum *= h
    return sum

def midpoint(f, a, b, n):
    h = float(b-a)/n
    for i in range(0, n):
        x = float(a + h/2) + i*h
        sum += f(x)        
    sum *= h
    return sum
    
    
    



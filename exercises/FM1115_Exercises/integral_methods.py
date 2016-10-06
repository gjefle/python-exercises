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
    sum = 0
    for i in range(0, n):
        x = float(a + h/2) + i*h
        sum += f(x)        
    sum *= h
    return sum


# Unit tests
def test_trapezoidal():    
    f = lambda x: 90*x**2 - 3*x**4
    start = 1
    end = 20
    resolution = 10000
    expected = -1680029.4
    tolerance = 0.1
    result = trapezoidal(f, start, end, resolution)
    diff = abs(expected - result)
    assert diff < tolerance, 'diff: %g, tol: %g' % (diff, tolerance)
    
def test_midpoint():
    f = lambda x: 90*x**2 - 3*x**4
    start = 1
    end = 20
    resolution = 10000
    expected = -1680029.4
    tolerance = 0.1
    result = midpoint(f, start, end, resolution)
    diff = abs(expected - result)
    assert diff < tolerance, 'diff: %g, tol: %g' % (diff, tolerance)
    
test_trapezoidal()
test_midpoint()
        
    



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
expected = 53.33333333
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
from math import sin, pi
f_sine = lambda x: sin(x)
a = 0
 # a)
b = pi
n = 2
print "Task 3.4 a):"
print midpoint(f_sine, a, b, n)
print trapezoidal(f_sine, a, b, n)

#b)
b = 2*pi
print midpoint(f_sine, a, b, n)
print trapezoidal(f_sine, a, b, n)

#Exercise 3.5 See integral_methods.py

#Exercise 3.6 Rounding errors
def test_trapezoidal_linear():
    f = lambda x: 6*(10**8)*x - 4*10**6
    F = lambda x: 3*(10**8)*x**2 - 4*(10**6)*x
    a = 1.2/6E8
    b = 4.4/6E8
    expected = F(b) - F(a)
    tol = 1E-14
    for n in 2,20,21:
        computed = trapezoidal(f,a,b,n)
        error = abs(expected - computed)
        success = error < tol
        msg = 'n=%d, err=%g' % (n, error)        
        assert success, msg
print "Task 3.6:"
test_trapezoidal_linear()

print "Convergence rates:"
def convergence_rates(f, F, a, b, num_experiments=14):
    from math import log
    from numpy import zeros
    expected = F(b) - F(a)
    n = zeros(num_experiments, dtype=int)
    E = zeros(num_experiments)
    r = zeros(num_experiments-1)
    for i in range(num_experiments):
        n[i] = 2**(i+1)
        computed = trapezoidal(f, a, b, n[i])
        E[i] = abs(expected - computed)
        if i > 0:
            r_im1 = log(E[i]/E[i-1])/log(float(n[i])/n[i-1])
            r[i-1] = float('%.2f' % r_im1) # Truncate to two decimals
    return r
def test_trapezoidal_conv_rate():
    """Check empirical convergence rates against the expected -2."""
    from math import exp
    V = lambda x: 6*(10**8)*x - 4*10**6
    v = lambda x: 3*(10**8)*x**2 - 4*(10**6)*x
    #v = lambda t: 3*(t**2)*exp(t**3)
    #V = lambda t: exp(t**3)
    a = 1.1; b = 1.9
    r = convergence_rates(v, V, a, b, 14)
    print r
    tol = 0.01
    msg = str(r[-4:]) # show last 4 estimated rates
    assert (abs(r[-1]) - 2) < tol, msg
test_trapezoidal_conv_rate()

# Exercise 3.10 Integrating x raised to x
from adaptive_integration import adaptive_integration
a = 0.0
b = 4.0
eps = 1E-4
f = lambda x: x**x
n_midpoint = adaptive_integration(f, a, b, eps, "midpoint")
print 'n_midpoint: %d' % (n_midpoint)
n_trapezoidal = adaptive_integration(f, a, b, eps, "trapezoidal")
print 'n_trapezoidal: %d' % (n_trapezoidal)



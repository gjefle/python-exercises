# -*- coding: utf-8 -*-

# Exercise 2.3
'''
import math
def circleCircumference(radius):
    return 2*math.pi*r;

def circleArea(r):
    return math.pi*r**2

r = input('r:')
print "Circumference: " + str(circleCircumference(r))
print "Area: " + str(circleArea(r))
'''
#Exercise 2.5 Area of a polygon
'''
import numpy
def polyArea(xValues, yValues): 
    val1=0
    val2=0
    xLength = len(xValues)
    yLength = len(yValues)
    if(xLength == yLength):
        for i in range(1, xLength):
            val1 += xValues[i-1]*yValues[i]
            val2 += yValues[i-1]*xValues[i]
        val1 += xValues[xLength-1] * yValues[0]
        val2 += yValues[yLength-1] * xValues[0]
        return 0.5*numpy.abs(val1-val2)
    else: 
        raise Exception("Length of xArray and yArray is not equal")
        
trianglePointsX = [0,2,3]
trianglePointsY = [0,3,0]
print "Triangle area: " + str(polyArea(trianglePointsX, trianglePointsY))

squarePointsX = [0, 0, 4, 4]
squarePointsY = [0, 8, 8, 0]
print "Square area: " + str(polyArea(squarePointsX, squarePointsY))

pentagonPointsX = [1, 2, 3.5, 4, 3]
pentagonPointsY = [1, 4, 5, 2.5, 1.25]
print "Polygon area (from figure): " + str(polyArea(pentagonPointsX, pentagonPointsY))
'''

# Exercise 2.6
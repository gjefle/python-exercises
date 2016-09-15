# -*- coding: utf-8 -*-

# Exercise 2.3
import math
def exercise_2_3():
    def circle_circumference(radius):
        return 2*math.pi*radius;

    def circle_area(radius):
        return math.pi*radius**2  
    
    radius = input('Type in radius:')
    print "Circumference: " + str(circle_circumference(radius))
    print "Area: " + str(circle_area(radius))

#Exercise 2.5 Area of a polygon

import numpy
def exercise_2_5():    
    def poly_area(x_values, y_values): 
        val1=0
        val2=0
        x_length = len(x_values)
        y_length = len(y_values)
        if(x_length == y_length):
            for i in range(1, x_length):
                val1 += x_values[i-1]*y_values[i]
                val2 += y_values[i-1]*x_values[i]
                val1 += x_values[x_length-1] * y_values[0]
                val2 += y_values[y_length-1] * x_values[0]
            return 0.5*numpy.abs(val1-val2)
        else: 
           raise Exception("Length of xArray and yArray is not equal")
        
    triangle_points_x = [0,2,3]
    triangle_points_y = [0,3,0]
    print "Triangle area: " + str(poly_area(triangle_points_x, triangle_points_y))

    square_points_x = [0, 0, 4, 4]
    square_points_y = [0, 8, 8, 0]
    print "Square area: " + str(poly_area(square_points_x, square_points_y))

    pentagon_points_x = [1, 2, 3.5, 4, 3]
    pentagon_points_y = [1, 4, 5, 2.5, 1.25]
    print "Polygon area (from figure): " + str(poly_area(pentagon_points_x, pentagon_points_y))


# Exercise 2.6 Average of integers
def exercise_2_6():
    def average_int(max_number):
        if(max_number > 1):
            sum = 0
            for i in range(1, max_number +1):
                sum+= i
            return float(sum) / max_number           
        else:
            raise Exception("number too low")
    N = 5
    print average_int(N)

# Run exercises here:
exercise_2_3()
exercise_2_5()
#exercise_2_6()

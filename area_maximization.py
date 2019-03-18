#!/usr/bin/python
#Get the optimal maximized area for the perimeter (total amount of wires for the fence)
#3 methods: Simple Algebra, Quadratic Equations, Derivative

import sys
import math 
from fractions import Fraction

perimeter = float(Fraction(input("Enter parameter / the total amount of wire ")))
horizontalFence = float(Fraction(input("Enter number of horizontal fences ")))
verticalFence = float(Fraction(input("Enter number of vertical fences ")))

def quadraticFunction(a,b,c):
    resultPositive = (-b + math.sqrt(b**2 - (4*a*c)) ) / (2*a)
    resultNegative = (-b - math.sqrt(b**2 - (4*a*c)) ) / (2*a)
    return resultPositive, resultNegative 

message = ""
def maximizeArea(perimeter, numberOfhorizontalFence,numberOfVerticalFence ):
    initialSide = perimeter / 4 
    length = 2 * initialSide / numberOfhorizontalFence 
    width = (perimeter - (numberOfhorizontalFence * length)) / numberOfVerticalFence  
    maxArea = length * width
    message = "The optimal maximum area is: " + str(maxArea)
    return message

print (maximizeArea(perimeter, horizontalFence, verticalFence ))

#print (quadraticFunction(-2/3, 100/3, 0))

# packing and unpaking values in tuple
Sue = ('Student',[89,94,85])
name, grades = Sue
print(name)
print(grades)
for note in grades:
    print(note, end=' ')

import math

math.sqrt(900)

def rectangle_area(length, width):
    """ return a rectangle's area"""
    return length * width

rectangle_area(width=10,length=3)
rectangle_area(2,6)

def average(*args):
    return sum(args) / len(args)

def calculate_product(*args):
    product = 1
    for value in args:
        product *= value
    return product

calculate_product(10,20,30)
calculate_product(*range(1,6,2))
#

s = 'Hello'
s.lower()
s.upper()

x = 7
def access_global():
    print('x printed from global scope:',x)

access_global()

def try_to_modify_global():
    x = 3.5
    print('x printed from try_to_modify_global:', x)
try_to_modify_global

def modify_global():
    global x
    x = 'hello'
    print('x printed from modify_global ', x)

modify_global()
x

from math import ceil, floor
ceil(10.3)
floor(10.3)
e = 'hello'
from math import *

import statistics as stats
grades = [85,49,89,58,78,98]
stats.mean(grades)

from decimal import Decimal as dec

val1 = dec('2.5')
val1 ** 0.5
math.sqrt(val1)

x = 7
def cube(number):
    print('id(number):', id(number))
    return number ** 3
cube(7)
def cube(number):
    print('number is x:', number is x) # x is a global variable
    return number ** 3

import statistics
statistics.pvariance([1,3,4,2,6,5,3,4,5,2])
statistics.pstdev([1,3,4,2,6,5,3,4,5,2])
math.sqrt(statistics.pvariance([1,3,4,2,6,5,3,4,5,2]))

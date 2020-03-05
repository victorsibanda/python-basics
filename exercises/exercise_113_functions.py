import math

def add_fun(x,y):
    return x+y


def subtract_fun(x,y):
    return x-y


def multiply_fun(x,y):
    return x * y


def divide_fun(x,y):
    return x/y


def power(x,y):
    return x**y


def area_of_circle(r) :
    result = math.pi * r**2
    return result


def area_of_square(x):
    result = x**2
    return result


def area_of_triangle(b,h):
    result = (0.5 * b * h)
    return result


def area_of_triangle2(a,b,c):
    result = (0.5 * a * b * math.sin(c))
    return result


def area_of_sphere(r) :
    result = 4 * math.pi * r**2
    return result


def hypotnuse_fun(a,b):
    result = ( a**2 + b**2 )**0.5
    return result


print (area_of_triangle2(10,20,90))


print (add_fun(10,820) == 830)
print ('Got:', add_fun(10,820))


print (power(10,2) == 100)
print ('Got:', power(10,2))
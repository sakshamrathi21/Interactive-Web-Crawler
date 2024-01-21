'''
    Geometry (Complex and Polar)
'''
import math
from complex import Complex
from polar import Polar
# import the classes


def modulus(c:Complex):
    '''return modulus of the complex number'''
    return ((c.x)**2 + (c.y)**2)**(1/2)
    

def arg(c:Complex):
    '''return arg (angle) of the complex number'''
    return math.atan(c.y/c.x)

    

def abscissa(p:Polar):
    '''return abscissa of the polar point'''
    return p.r*math.cos(p.t)
    

def ordinate(p:Polar):
    '''return ordinate of the polar point'''
    return p.r*math.sin(p.t)
    

def distance(z1:Complex, z2:Complex):
    '''distance between points'''
    return ((z1.x-z2.x)**2 + (z1.y-z2.y)**2)**(1/2)
    

if __name__ == '__main__':

    # you can use this area of code to check all the functions manually
    # one example of using the functions has been shown
    # run this using "python3 main.py"
    a = Complex(1,2)
    b = Complex(2,2)
    z = a + b # uses the overloaded add
    print(z)
    # print(modulus(z)) # you can call after you implement
    x = Polar(2,math.pi/3) # uses the overloaded power
    print(x ** 2)

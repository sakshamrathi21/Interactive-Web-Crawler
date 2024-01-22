'''
    Geometry (Complex and Polar)
'''
import math

class Complex:

    def __init__(self, a, b):
        self.real = a  
        self.imag = b  

    def __str__(self):
        return f"{self.real} + i{self.imag}"

    def __add__(self, a):
        return Complex(self.real + a.real, self.imag + a.imag)

    def __sub__(self, a):
        return Complex(self.real - a.real, self.imag - a.imag)


class Polar:

    def __init__(self, a, b):
        self.r = a
        self.t = b

    def __str__(self):
        return f"({self.r},{self.t})"

    def __mul__(self, a):
        return Polar(round(self.r * a.r,2), round(self.t + a.t,2))

    def __pow__(self, a):
        return Polar(round(self.r ** a,2), round(self.t * a,2))


def modulus(c: Complex) -> float:
    '''return modulus of the complex number'''
    return abs(c)

def arg(c: Complex) -> float:
    '''return arg (angle) of the complex number'''
    return math.atan2(c.imag, c.real)

def abscissa(p: Polar) -> float:
    '''return abscissa of the polar point'''
    return p.r * math.cos(p.theta)

def ordinate(p: Polar) -> float:
    '''return ordinate of the polar point'''
    return p.r * math.sin(p.theta)

def distance(z1: Complex, z2: Complex) -> float:
    '''distance between points'''
    return abs(z1 - z2)

if __name__ == '__main__':
   
    a = Complex(1,2)
    b = Complex(2,2)
    z = a + b 
    print(z)
    print(f"Modulus: {modulus(z)}")
    x = Polar(2, math.pi/3) 
    print(x ** 2)
    print(f"Abscissa: {abscissa(x)}")
    print(f"Ordinate: {ordinate(x)}")
    print(f"Distance: {distance(a, b)}")

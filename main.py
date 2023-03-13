import math

import sympy
from sympy import *

def task1():
    x = -1.23
    y = sympy.sqrt(8)
    A = ((7 * x * y)/4) * (x + y) - (pow((x - y), 2))
    print(sympy.simplify(A))



def task2():
    x = Symbol('x')
    y = Symbol('y')
    A = ((7 * x * y)/4) * (x + y) - (pow((x - y), 2))
    print(sympy.diff(A, x))
    print(sympy.diff(A, y))


def task3():
    x = Symbol('x')
    y = Symbol('y')
    A = ((7 * x * y) / 4) * (x + y) - (pow((x - y), 2))
    print(sympy.integrate(A, x))

def task4():
    x = 2
    y = Symbol('y')
    A = ((7 * x * y) / 4) * (x + y) - ((x - y)**2)
    print(sympy.solveset(sympy.Eq(A, 0), y))

def task5():
    x1 = Symbol('x1')
    x2 = Symbol('x2')
    x3 = Symbol('x3')
    A = 3 * x1 + 4 * x2 - x3
    B = 4 * x1 - 5 * x2 + 3 * x3
    C = 2 * x1 - 3 * x2 - 4 * x3
    print(sympy.linsolve([sympy.Eq(A, 2), sympy.Eq(B, 7), sympy.Eq(C, -2)], (x1, x2 , x3)))

def task6():
    x = Symbol('x')
    A = sympy.exp(2 * x) * sympy.cos(x)
    print(sympy.integrate(A, (x, 0, math.pi/2)))

def task7():
    x = Symbol('x')
    A = 1/(x**2 + 4 * x + 9)
    print(sympy.integrate(A, (x, -math.inf, math.inf)))

if __name__ == '__main__':
    task7()
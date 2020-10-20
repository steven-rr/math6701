# ////////////////////////////////////////////////////////////////////////////
# //|
# //| Author : Steven Rivadeneira
# //|
# //| File Name : p8.py
# //|
# //| Description : Graphs transformation.
# //|
# //| Notes :
# //|
# //|
# //|
# //|
# ////////////////////////////////////////////////////////////////////////////

from math import cos
from math import sin
from math import pi
from math import sqrt
import matplotlib.pyplot as plt

# lambda1 = -0.5
# lambda2 = -2
def linear_transform_A1(x,y):
    lambda1 = -2
    lambda2 = -0.5
    result = [ lambda1*x,  lambda2*y]
    return result

# lamba = -2
def linear_transform_A2(x, y):
    lambda_ = -2
    result = [lambda_*x + y, lambda_*y]
    return result

# lambda = 1.5
# mu =  2
def linear_transform_A3(x, y):
        lambda_ = 1.5
        mu = 2
        result =  [ lambda_*x - mu*y, mu*x + lambda_*y]
        return result

def main():
        A1x = []
        A1y = []
        A2x = []
        A2y = []
        A3x = []
        A3y = []
        x_ = []
        y_ = []

        for theta in range(0, 201, 1):
                #change step size
                theta = -pi/2 + pi*(theta/100)
                #calc transformation by A1.
                x = cos(theta)
                y = sin(theta)
                #debug:
                x_.append(x)
                y_.append(y)
                #end debug
                A1 = linear_transform_A1(x,y)
                A1x.append(A1[0])
                A1y.append(A1[1])

                #calc transformation by A2.
                A2 = linear_transform_A2(x,y)
                A2x.append(A2[0])
                A2y.append(A2[1])
                #calc transformation by Tinv L T
                A3 = linear_transform_A3(x,y)
                A3x.append(A3[0])
                A3y.append(A3[1])

        #plot
        plt.figure(1)
        plt.title("Problem 8 part a, this is codomain of x^2 + y ^2 = 1")
        plt.axis("equal")
        plt.plot(A1x, A1y, 'b')

        plt.figure(2)
        plt.title("Problem 8 part b, this is codomain of x^2 + y ^2 = 1")
        plt.axis("equal")
        plt.plot(A2x, A2y, 'b')

        plt.figure(3)
        plt.title("Problem 8 part c, this is codomain of x^2 + y ^2 = 1")
        plt.axis("equal")
        plt.plot(A3x, A3y, 'b')
        plt.show()


if __name__ == "__main__":
        main()
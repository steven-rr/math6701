# ////////////////////////////////////////////////////////////////////////////
# //|
# //| Author : Steven Rivadeneira
# //|
# //| File Name : p6.py
# //|
# //| Description : Graphs linear transformation.
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

def linear_transform(x, y):
        result =  [2*x + y, 3*y]
        return result

def main():
        LTx_plus = []
        LTy_plus= []

        LTx_minus = []
        LTy_minus = []
        for theta in range(0, 101, 1):
                #change step size
                theta = pi*(theta/100)
                #calc
                LT = linear_transform(cos(theta),sin(theta))
                LTx_plus.append(LT[0])
                LTy_plus.append(LT[1])

        for theta in range(0, 101, 1):
                # change step size.
                theta = pi + pi*(theta/100)
                #calc
                LT = linear_transform(cos(theta),sin(theta))
                LTx_minus.append(LT[0])
                LTy_minus.append(LT[1])

        #calc values.
        point1 = linear_transform(1,0)
        point2 = linear_transform(1/sqrt(2), 1/sqrt(2))
        #plot
        plt.figure(1)
        plt.plot(LTx_plus, LTy_plus, 'b')
        plt.plot(LTx_minus, LTy_minus, 'r')
        plt.plot(point1[0], point1[1] , 'ro', label = "point (1,0)")
        plt.plot(point2[0], point2[1] , 'bo', label = "point (1/sqrt2, 1/sqrt2)")
        plt.legend(loc="upper left")
        plt.show()


if __name__ == "__main__":
        main()
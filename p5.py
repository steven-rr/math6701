# ////////////////////////////////////////////////////////////////////////////
# //|
# //| Author : Steven Rivadeneira
# //|
# //| File Name : p5.py
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

def linear_transform_Tinv(x,y):
    result = [(1/5)*(x*sqrt(5) - 2*y*sqrt(5)), (1/5)*(2*x*sqrt(5) + y*sqrt(5))]
    return result
def linear_transform_L(x, y):
    result = [(2*x + 2*y), (2*x - y)]
    return result
def linear_transform_T(x, y):
        result =  [ (1 / sqrt(5)) * (x + 2*y), (1 / sqrt(5))*(-2*x + y)]
        return result

def main():
        Tx_plus = []
        Ty_plus= []
        LTx_plus = []
        LTy_plus = []
        TLTx_plus = []
        TLTy_plus = []

        Tx_minus = []
        Ty_minus = []
        LTx_minus = []
        LTy_minus = []
        TLTx_minus = []
        TLTy_minus = []


        for theta in range(0, 101, 1):
                #change step size
                theta = -pi/2 + pi*(theta/100)
                #calc transformation by T.
                x = cos(theta)
                y = sin(theta)
                T = linear_transform_T(x,y)
                Tx_plus.append(T[0])
                Ty_plus.append(T[1])
                #calc transformation by L * T.
                LT = linear_transform_L(T[0],T[1])
                LTx_plus.append(LT[0])
                LTy_plus.append(LT[1])
                #calc transformation by Tinv L T
                TLT = linear_transform_Tinv(LT[0], LT[1])
                TLTx_plus.append(TLT[0])
                TLTy_plus.append(TLT[1])

        for theta in range(0, 101, 1):
                # change step size.
                theta = pi/2 + pi*(theta/100)
                #calc transformation by T.
                T = linear_transform_T(cos(theta),sin(theta))
                Tx_minus.append(T[0])
                Ty_minus.append(T[1])
                #calc transformation by L * T
                LT = linear_transform_L(T[0], T[1])
                LTx_minus.append(LT[0])
                LTy_minus.append(LT[1])
                #calc transformation by Tinv L T
                TLT = linear_transform_Tinv(LT[0], LT[1])
                TLTx_minus.append(TLT[0])
                TLTy_minus.append(TLT[1])
        #plot
        plt.figure(1)
        plt.axis("equal")
        plt.plot(Tx_plus, Ty_plus, 'r')
        plt.plot(Tx_minus, Ty_minus, 'b')
        plt.figure(2)
        plt.axis("equal")
        plt.plot(LTx_plus, LTy_plus, 'r')
        plt.plot(LTx_minus, LTy_minus, 'b')
        plt.figure(3)
        plt.axis("equal")
        plt.plot(TLTx_plus, TLTy_plus, 'r')
        plt.plot(TLTx_minus, TLTy_minus, 'b')
        plt.legend(loc="upper left")
        plt.show()


if __name__ == "__main__":
        main()
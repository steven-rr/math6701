import numpy as np
from math import cos
from math import sin
from math import pi
import matplotlib.pyplot as plt

# (2x + y)
#   (y)

# (2 1) (x) =  (2x + y)
# (0 1) (y)       (y)
LTx_plus = []
LTy_plus= []

LTx_minus = []
LTy_minus = []
for theta in range(0, 101, 1):
        #change step size
        theta = pi*(theta/100)
        #calc
        LTx_plus.append(2*cos(theta) + sin(theta))
        LTy_plus.append(sin(theta))

for theta in range(0, 101, 1):
        # change step size.
        theta = pi + pi*(theta/100)
        #calc
        LTx_minus.append(2*cos(theta) + sin(theta))
        LTy_minus.append(sin(theta))

#plot
plt.figure(1)
plt.plot(LTx_plus, LTy_plus, 'b')
plt.plot(LTx_minus, LTy_minus, 'r')
plt.show()

# # V = aA  +  bB
# # current problem:
# # 3 = 2a  +  3b
# # 5 =  a  + -2b
#
# V = np.array([4,11])
# A = np.array([7,13])
# B = np.array([3,-2])
#
# n = np.cross(V,B)
# a = np.dot(np.cross(B,V), n) #/ np.dot(np.cross(B,A),g)
# a_cramer = (B[1]*V[0] - B[0]*V[1]) / (A[0]*B[1] - A[1]*B[0])
# b_cramer = (A[0]*V[1] - A[1]*V[0]) / (A[0]*B[1] - A[1]*B[0])


######

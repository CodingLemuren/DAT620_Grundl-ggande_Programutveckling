from matrix import *
import sys
import matplotlib.pyplot as plt

data_file = sys.argv[1]

X, Y = transpose(loadtxt(data_file))
print("X:", X)
print("Y:", Y)
Xp = powers(X,0,1)
Yp = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

Y2 = [(m*x + b) for x in X]

print("Beta hatt:",b)
print("m:", m)

plt.plot(X,Y, 'ro')
plt.plot(X,Y2)
plt.show()
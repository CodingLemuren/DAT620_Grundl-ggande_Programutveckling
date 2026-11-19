import sys
import matplotlib.pyplot as plt
import numpy as np


def powers(list,power_start,power_finish):
    M = [[0 for _ in range(power_finish-power_start+1)] for _ in range(len(list))]
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = list[i]**(power_start+j)
    M = np.array(M)
    return M


data_file = sys.argv[1]
degree = int(sys.argv[2])

X, Y = np.transpose(np.loadtxt(data_file))
print("X:", X)
print("Y:", Y)
Xp = powers(X,0,degree)
Yp = powers(Y,1,1)
Xpt = np.transpose(Xp)

a = np.matmul(np.linalg.inv(np.matmul(Xpt,Xp)),np.matmul(Xpt,Yp))
print("a before:", a)

a = a[:,0]
print("a:", a)

def poly(a,X):
    Y2 = []
    for x in X:
        y = 0
        for i,k in enumerate(a):
            y += k*x**(i)
        Y2.append(y)
    return Y2

X2 = np.linspace(int(X[0]),int(X[-1]),int((X[-1]-X[0])/0.2)).tolist()

plt.plot(X,Y,'ro')
plt.plot(X2,(poly(a,X2)))
plt.show()

#print("Beta hatt:",b)
""" print("m:", m)

plt.plot(X,Y, 'ro')
plt.plot(X,Y2)
plt.show() """
def transpose(M):
    transposed_M = [[0 for _ in range(len(M))] for _ in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[i])):
            transposed_M[j][i] = M[i][j]
    return transposed_M
M = [[1,2]
     ,[3,4]
     ,[4,8]
     ]
print(transpose(M))

def powers(list,power_start,power_finish):
    pass

def matmul():
    pass

def invert():
    pass

def loadtxt():
    pass



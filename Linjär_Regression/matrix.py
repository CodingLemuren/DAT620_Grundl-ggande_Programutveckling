def transpose(M):
    transposed_M = [[0 for _ in range(len(M))] for _ in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[i])):
            transposed_M[j][i] = M[i][j]
    return transposed_M


#Test for transpose function
""" M = [[1,2]
     ,[3,4]
     ,[4,8]
     ]
print(transpose(M)) """

def powers(list,power_start,power_finish):
    M = [[0 for _ in range(power_finish-power_start+1)] for _ in range(len(list))]
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = list[i]**(power_start+j)
    return M

#Test for powers function
""" test_list = [2,3,4]
power_start, power_finish = 0,2
print(powers(test_list,power_start,power_finish)) """

def matmul():
    pass

def invert(M):
    a = M[0][0]
    b = M[0][1]
    c = M[1][0]
    d = M[1][1]
    det = (a*d-b*c)
    inverted_M = [[d/det, -b/det]
                  ,[-c/det, a/det]]
    return inverted_M

#Test for invert function
""" A    = [[1,2]
        ,[3,4]]
print(invert(A)) """

def loadtxt(M_file):
    read_M_file = open(M_file, "r")
    M = []
    for line in read_M_file:
        M.append([float(x) for x in line.split()])
    return M

#Test for loadtxt function
# file = open("Linjär_Regression/chirps.txt", "r")
#print(loadtxt("Linjär_Regression/chirps.txt"))

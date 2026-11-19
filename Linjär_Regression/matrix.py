def transpose(M):
    if M == []:
        return []
    transposed_M = [[0 for _ in range(len(M))] for _ in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[i])):
            transposed_M[j][i] = M[i][j]
    return transposed_M

def powers(list,power_start,power_finish):
    M = [[0 for _ in range(power_finish-power_start+1)] for _ in range(len(list))]
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] = list[i]**(power_start+j)
    return M

def matmul(A, B):
    if A == [] or B == []:
        return []
    rows_a = len(A)
    cols_a = len(A[0])
    cols_b = len(B[0])
    rows_b = len(B)

    if cols_a is not rows_b:
        print("matrix mult not possible")
        return
    C = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    k = 0
    len(A[0])
    for j in range(cols_b):
        for i in range (rows_a):
            for k in range(rows_b): # summa där k går från 0 till len(A[0]) Aik *Bkj
                C[i][j] += A[i][k] * B[k][j]
    return C

def invert(M):
    a = M[0][0]
    b = M[0][1]
    c = M[1][0]
    d = M[1][1]
    det = (a*d-b*c)
    inverted_M = [[d/det, -b/det]
                  ,[-c/det, a/det]]
    return inverted_M

def loadtxt(M_file):
    read_M_file = open(M_file, "r")
    M = []
    for line in read_M_file:
        M.append([float(x) for x in line.split()])
    return M
def Transpose1(M):
    T = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    return T

def Transpose(A):
    T = []
    for i in range(len(A[0])):
        temp = []
        for j in range(len(A)):
            temp.append(A[j][i])
        T.append(temp)
    return T

mat = [[1,2,3],[4,5,6],[7,8,9]]
T = Transpose(mat)
print(mat,T)
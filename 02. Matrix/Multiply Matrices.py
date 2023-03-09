def multiply(A, B, C, n):
    # Code here
    for i in range(len(C)):
        for j in range(len(C[0])):
            for k in range(len(B)):
                C[i][j]+=A[i][k]*B[k][j]
    return C


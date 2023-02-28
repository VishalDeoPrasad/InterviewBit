def dotProject(A, B):
    dot = 0
    for i in range(len(A)):
        temp_sum = 0
        for j in range(len(A[0])):
            temp_sum += (A[i][j]*B[j][i])
        dot += temp_sum
        temp_sum = 0
    return dot
    

A = [[1,1,2], [2,1,6], [3,1,5]]
B = [[3,1,2], [2,1,1], [5,2,4]]

X = [[1,2,3], [4,5,6], [7,8,9]] 
Y = [[9,8,7], [6,5,4], [3,2,1]]

print(dotProject(A, B))


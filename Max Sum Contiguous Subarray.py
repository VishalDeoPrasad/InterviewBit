#Find the contiguous subarray within an array, A of length N which has the largest sum.

#Idea 1 - Brute force Soluction 
#TC - O(N*N), SC - O(1)
def MaxSum(A):
    maxx = 0
    for i in range(len(A)):
        for j in range(len(A)):
            cur_max = 0
            for k in range(i, j+1):
                cur_max += A[k]
            if cur_max > maxx:
                maxx = cur_max
    return maxx




A1 = [1, 2, 3, 4, -10]
A2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(MaxSum(A2))
class Solution:
    def Transpose(self, A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    
    def reverse(self, A):
        n = len(A)
        for i in range(n//2):
            j = n-i-1
            A[i], A[j] = A[j], A[i]
        return A
    
        
    def solve(self, A):
        T = self.Transpose(A)
        for i in range(len(T)):
            T[i] = self.reverse(T[i])
        return T

m = [[1,2],[3,4]]
mat = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]
mat1 = [[1,2,3],[4,5,6],[7,8,9], [10,11,2]]
mat2 = [[1,2],[5,6],[8,9], [11,12]]
n =  [
    [3, 1],
    [4, 2]
 ]
# print(mat)
# print(Rotation().Transpose(mat))
print(Solution().solve(n))

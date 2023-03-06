class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        row = len(A)
        col = len(A[0])
        for i in range(row):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        return A
A = [[1, 0], [1, 0]]             
print(Solution().solve(A))
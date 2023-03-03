class Solution:
    def solve1(self, A, B):
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = A[i][j] - B[i][j]
        return A
    
    def solve(self, A, B):
        N = len(B)
        M = len(B[0])
        C = []
        for i in range(0, N):
            C.append([0] * M)
        for i in range(0, N):
            for j in range(0, M):
                C[i][j] = A[i][j] - B[i][j]

        return C
    
A =  [[1, 2, 3], 
      [4, 5, 6], 
      [7, 8, 9]]

B =  [[9, 8, 7], 
      [6, 5, 4], 
      [3, 2, 1]]

print(Solution().solve(A, B))
class Solution:
    def solve(self, A, B, C):
        allowed = B%2
        fine = 0
        for i in range(len(A)):
            if A[i]%2 != allowed:
                fine += C 
        return fine

A = [1, 2, 3]
B = 31
C = 100
print(Solution().solve(A,B,C))
            
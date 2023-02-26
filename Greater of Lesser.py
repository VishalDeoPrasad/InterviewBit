class Solution:
    def solve(self, A, B, C):
        more = 0
        less = 0
        for a in A:
            if a > C:
                more += 1
        for b in B:
            if b < C:
                less += 1
        return max(more, less)
    
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
C = 3
print(Solution().solve(A,B,C))
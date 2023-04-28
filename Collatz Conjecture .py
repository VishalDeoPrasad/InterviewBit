class Solution:
    def solve(self, A, B):
        for _ in range(B-1):
            if A % 2 == 0:
                A = A//2
            else:
                A = 3*A+1
        return A
    
print(Solution().solve(5, 6))
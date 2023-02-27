class Solution:
    def solve(self, A, B):
        for i in range(1, B):
            if A%2==0:
                A = A//2
            else:
                A = (A*3)+1
        return A
    
print(Solution().solve(5,6))

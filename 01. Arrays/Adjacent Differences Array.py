class Solution:
    def solve(self, A):
        result = [A[i+1] - A[i] for i in range(len(A)-1)]
        return result
print(Solution().solve([6, 2, 4, 4, 3]))
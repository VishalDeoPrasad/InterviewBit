class Solution:
    def solve(self, A):
        A.sort()
        min_diff = float('inf')
        for i in range(len(A)-1):
            if abs(A[i]-A[i+1]) < min_diff:
                min_diff = abs(A[i]-A[i+1])
        return min_diff

print(Solution().solve([1,2,3,4,5]))
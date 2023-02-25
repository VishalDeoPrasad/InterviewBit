class Solution:
    def solve(self, A):
        mean = sum(A)/len(A)
        variance = 0
        for i in range(len(A)):
            variance += (A[i] - mean)**2
        return '{:.2f}'.format(variance/len(A))
A = [99, 81, 4, 74, 9, 79, 45, 25, 44, 86]
print(Solution().solve(A))
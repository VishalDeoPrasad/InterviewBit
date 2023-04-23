class Solution:
    def solve(self, A):
        n = len(A)
        mean = sum(A)/n
        result = 0
        for i in range(len(A)):
            result += (A[i]-mean)**2
        return round(result/n, 2)

A = [99, 81, 4, 74, 9, 79, 45, 25, 44, 86]
print(Solution().solve(A))
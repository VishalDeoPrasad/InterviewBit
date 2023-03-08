class Solution:
    def maxProfit(self, A):
        if not A: return 0

        max_profit = 0
        for i in range(1, len(A)):
            if A[i]>A[i-1]:
                max_profit += A[i]-A[i-1]
        return max_profit

A = [5, 2, 10]
print(Solution().maxProfit(A))
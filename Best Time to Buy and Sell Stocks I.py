class Solution:
    def maxProfit(self, A):
        if not A:
            return 0
        max_profit = 0
        min_so_far = A[0]
        for i in range(len(A)):
            if A[i] < min_so_far:
                min_so_far = A[i]
            if A[i]-min_so_far > max_profit:
                max_profit = A[i]-min_so_far
        return max_profit

print(Solution().maxProfit([1, 4, 5, 2, 4]))
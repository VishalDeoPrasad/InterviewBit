class Solution:
    def solve(self, A):
        m = 1000000007
        ways = 2
        for i in range(2, A + 1):
            ways = ways * i
            ways = ways % m
        return ways
print(Solution().solve(2))

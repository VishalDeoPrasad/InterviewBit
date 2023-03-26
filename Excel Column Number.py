class Solution:
    def solve(self, excel):
        n = len(excel)
        res = 0
        for i in range(n):
            j = n-i-1
            res += (ord(excel[i])-64)*(26**j)
        return res

print(Solution().solve("BZC"))
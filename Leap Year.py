class Solution:
    def solve(self, A):
        if A%4 == 0:
            if A%100 == 0:
                if A%400 == 0:
                    return 1
                else:
                    return 0
            else:
                return 1
        else:
            return 0

print(Solution().solve(2020))

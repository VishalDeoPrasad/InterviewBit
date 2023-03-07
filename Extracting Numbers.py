import re
class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):
        summ = 0
        pattern = r"\d+"
        num = re.findall(pattern, A)
        for i in num:
            summ += int(i)
        return summ

print(Solution().solve("a12b34c"))
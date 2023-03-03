class Solution:
    def solve(self, A, B, C):
        B = B%2
        amt = 0
        for n in A:
            if n%2 != B:
                amt += C 
        return amt

print(Solution().solve([1, 2, 3, 4], 31, 100))
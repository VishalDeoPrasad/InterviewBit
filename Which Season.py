class Solution:
    def solve(self, A):
        if A >= 3 and A <= 5:
            return "Spring"
        elif A >= 6 and A <= 8:
            return "Summer"
        elif A >= 9 and A <= 11:
            return "Autumn"
        elif A <=12:
            return "Winter"
        else:
            return "Invalid"

print(Solution().solve(2))

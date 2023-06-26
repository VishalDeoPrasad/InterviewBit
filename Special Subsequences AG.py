class Solution:
    def solve(self, A):
        cnt = 0
        ans = 0
        for i in range(len(A)):
            if A[i] == "A":
                cnt += 1
            elif A[i] == "G":
                ans += cnt
        return ans
    
print(Solution().solve("ABCGAG"))
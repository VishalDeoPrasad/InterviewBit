class Solution:
    def title(self, A):
        n = A
        ans = ""
        while n>0:
            a = (n-1)%26
            ans = chr(65+a)+ans     
            n = (n-1)//26
        return ans
    def solve(self, A):
        ans = self.title(A)
        return ans

print(Solution().solve(1))
print(Solution().solve(2))
print(Solution().solve(25))


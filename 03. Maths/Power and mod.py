class Solution:
    def power(self, a,n,p):
        ans = 1
        for i in range(1, n+1):
            ans = (ans*a)%p
        return ans%p
    
print(Solution().power(10, 2, 3))

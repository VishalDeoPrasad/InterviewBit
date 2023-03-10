class Solution:
    def climbStairs(self, A):
        if A==1:
            return 1
        if A==2:
            return 2
        else:
            return self.climbStairs(A-1)+self.climbStairs(A-2)
print(Solution().climbStairs(5))
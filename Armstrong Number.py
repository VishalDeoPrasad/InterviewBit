class Solution:
    def solve(self, A):
        n = A
        p = len(str(A))
        arm_sum = 0
        while n>0:
            a = n%10
            arm_sum += a**p
            n = n//10
        return 1 if arm_sum == A else 0

print(Solution().solve(371))
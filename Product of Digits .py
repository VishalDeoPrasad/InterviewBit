class Solution:
    def solve(self, A):
        if A == 0:
            return 0
        prod = 1
        while A>0:
            a = A%10
            prod *= a 
            A = A//10
        return prod
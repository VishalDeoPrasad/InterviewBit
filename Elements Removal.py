class Solution:
    def solve(self, A):
        A.sort(reverse=True)
        cost = 0
        for i in range(0, len(A)):
            cost += A[i]*(i+1) 
        return cost
    
print(Solution().solve([8,10,0]))
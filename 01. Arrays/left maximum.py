class Solution:
    def solve(self, A):
        left_max = []
        left_max.append(A[0])
        for i in range(1,len(A)):
            left_max.append(max(left_max[i-1], A[i]))
        return left_max

print(Solution().solve([3,2,4,1,2,-1,3,0,1]))
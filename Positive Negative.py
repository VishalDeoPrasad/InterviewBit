class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        pos = 0
        neg = 0
        for i in range(len(A)):
            if A[i] > 0:
                pos += 1
            elif A[i] < 0:
                neg += 1
        return [pos, neg]
    
print(Solution().solve([-1,0,1]))
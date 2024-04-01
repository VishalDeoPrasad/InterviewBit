class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        cnt = 0
        for i in range(len(A)):
            if A[i] <= B:
                cnt += 1
        return cnt
            
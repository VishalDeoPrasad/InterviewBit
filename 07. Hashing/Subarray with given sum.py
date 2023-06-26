class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        for i in range(len(A)):
            for j in range(i, len(A)):
                print(sum(A[i:j+1]))
                

print(Solution().solve([1, 2, 3, 4, 5], 5))
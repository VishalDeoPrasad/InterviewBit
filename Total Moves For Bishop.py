class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return min(B-1, A-1)+min(B-1, 8-A)+min(8-B, A-1)+min(8-B, 8-A)

print(Solution().solve(4,4))
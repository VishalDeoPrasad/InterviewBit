class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        left, right = 0, len(A)-1
        mid = 0
        cnt = 0
        while left <= right:
            mid = (left+right)//2
            if A[mid] <= B:
                cnt = mid+1
                left = mid+1   
            else:
                right = mid - 1
        return cnt 
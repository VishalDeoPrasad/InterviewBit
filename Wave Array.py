class Solution:
    def wave(self, A):
        A.sort()
        for i in range(1, len(A), 2):
            A[i] , A[i-1] = A[i-1], A[i]

        return A
    
print(Solution().wave([4,3,8,9,4]))



class Solution:
    def solve(self, A):
        even, odd = 0, 0
        cnt = 0
        for i in range(len(A)):
            B = A.copy()
            B.pop(i)
            for j in range(len(B)):
                if j % 2 == 0:
                    even += B[j]
                else:
                    odd += B[j]
            if even == odd:
                cnt += 1
            even = 0
            odd = 0
        return cnt
    
print(Solution().solve([2,1,4,6]))
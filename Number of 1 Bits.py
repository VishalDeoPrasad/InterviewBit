class Solution:
    def numSetBits(self, N):
        cnt = 0
        while N>0:
            a = N&1
            cnt += a
            N = N>>1
        return cnt

print(Solution().numSetBits(11))
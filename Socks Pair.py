class Solution:
    def solve(self, A):
        A.sort()
        n = len(A)
        pair = 0
        i = 0
        j = 0
        while j < n:
            cnt = 0
            while A[i] == A[j]:
                j += 1
                cnt += 1
                if j == n:
                    pair += cnt//2
                    return pair
            pair += cnt//2
            i = j
        return pair
print(Solution().solve([1,1,2,2,3]))
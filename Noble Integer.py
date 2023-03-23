class Solution:
    def solve(self, A):
        unique = set(A)
        for num in unique:
            cnt = 0
            for a in A:
                if a > num:
                    cnt += 1
            if cnt == num:
                return 1
        return -1
    
A = [1, 1, 3, 3]
print(Solution().solve(A))
class Solution:
    def solve(self, A, B):
        if 'a' not in A:
            return 0
        i = 0
        maxx = 0
        n = len(A)
        while i < n:
            j = i+B
            if j <= n:
                a = A[i:j].count("a")
                if a > maxx:
                    maxx = a
                i = j
            else:
                a = A[i:].count("a")
                if a > maxx:
                    maxx = a
                return maxx
        return maxx
    
print(Solution().solve("baab", 2))
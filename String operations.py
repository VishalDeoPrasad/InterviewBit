class Solution:
    def solve(self, A):
        A = A*2
        ans = ""
        for ch in A:
            if ord(ch) >=97 and ord(ch) <= 122:
                if ch in ('a','e','i','o','u'):
                    ans += '#'
                else:
                    ans += ch

        return ans
    
print(Solution().solve("AbcaZeoB"))

class Solution:
    def solve(self, A):
        A = "".join(s for s in A)
        for i in range(97, 123):
            if chr(i) not in A:
                return 0
        return 1
    
A = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print(Solution().solve(A))

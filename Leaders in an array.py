class Solution:
    def solve(self, A):
        n = len(A)
        max_elem = []
        max_elem.append(A[n-1])
        for i in range(len(A)-1, -1, -1):
            if A[i] > max_elem[-1]:
                max_elem.append(A[i])
        return max_elem
    
print(Solution().solve([16, 17, 4, 3, 5, 2]))
                
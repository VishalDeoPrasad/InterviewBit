class Solution:
    #time complexity o(n*n)
    def solve1(self, A): 
        for i in range(len(A)): 
            if i == len(A)-1: 
                if sum(A[:i]) == 0:
                    return i
            else:
                if sum(A[:i]) == sum(A[i+1:]):
                    return i
        return -1
    
    def prefixArray(self, A):
        pf = []
        pf.append(A[0])
        for i in range(1, len(A)):
            pf.append(pf[i-1] + A[i])
        return pf

    def solve(self, A):
        pf = self.prefixArray(A)
        for i in range(len(A)):
            if i == 0:
                left = 0
                right = pf[len(A)-1] - pf[i]
                if left == right:
                    return i
            else:
                left  = pf[i-1]
                right = pf[len(A)-1] - pf[i]
                if left == right:
                    return i
    
print(Solution().solve([-7, 1, 5, 2, -4, 3, 0]))
print(Solution().prefixArray([-7, 1, 5, 2, -4, 3, 0]))
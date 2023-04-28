class Solution:
    def solve(self, A):
        even_pf = [A[0]]
        odd_pf = [A[1]]
        for i in range(2, len(A)):
            if i % 2 == 0:
                even_pf.append(even_pf[-1]+A[i])
            else:
                odd_pf.append(odd_pf[-1]+A[i])
        return even_pf, odd_pf
    
print(Solution().solve([2, 1, 6, 4]))
        


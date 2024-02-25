class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        count_odd = sum(1 for i in range(len(A)) if A[i]%2 != 0)
                
        return 1 if count_odd == 0 else (2 ** count_odd - 1) % (10 ** 9 + 7)
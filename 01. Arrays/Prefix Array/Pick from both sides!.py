class Solution:
    def prefixSum(self,A,B):
        aux = []
        curr = sum(A[:B])
        aux.append(curr)
        for i in range(B, len(A)):
            curr = curr+A[i]-A[i-B]
            aux.append(curr)
        return aux
            
        
    def solve(self, A, B):
        B = len(A)-B
        aux = self.prefixSum(A,B)
        return sum(A)-min(aux)
    
A = [5, -2, 3 , 1, 2]
B = 3

print(Solution().solve(A,B))

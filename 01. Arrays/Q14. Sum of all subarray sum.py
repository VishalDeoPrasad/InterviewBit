class Solution:
    def subarraySum(self, A):
        n = len(A)
        total_sum = 0
        for i in range(n):
            for j in range(i, n):
                #print((i,j), end="  ")
                #print(sum(A[i:j+1]), end="  ")
                #print(A[i:j+1])
                total_sum += sum(A[i:j+1])
        return total_sum

print(Solution().subarraySum([2,1,3]))
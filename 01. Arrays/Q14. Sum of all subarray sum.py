class Solution:
    def subarraySum2(self, A):
        n = len(A)
        total_sum = 0
        for i in range(n):
            for j in range(i, n):
                #print((i,j), end="  ")
                #print(sum(A[i:j+1]), end="  ")
                #print(A[i:j+1])
                total_sum += sum(A[i:j+1])
        return total_sum

    def subarraySum1(self, A):
        n = len(A)
        total_sum = 0
        for i in range(n):
            sumi = 0
            for j in range(i, n):
                sumi += A[j]
                total_sum += sumi

        return total_sum
    
    def subarraySum(self, A):
        result = 0
        n = len(A)
        for i in range(0, n):
            result += (A[i] * (1+i) * (n-i))
        return result

print(Solution().subarraySum([1,2,3]))

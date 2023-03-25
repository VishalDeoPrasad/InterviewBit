class Solution:
    def solve1(self, A):
        max_subarray = []
        max_sum = 0
        for i in range(len(A)):
            if A[i] < 0:
                continue
            for j in range(i,len(A)):
                if A[j] < 0:
                    break
                temp_sum = sum(A[i:j+1])
                if temp_sum > max_sum:
                    max_sum = temp_sum
                    max_subarray = A[i:j+1]
        return max_subarray
    def solve(self, A):
        i,j = 0,0
        while j < len(A):
            while A[j] >= 0:
                j += 1
            print(sum(A[i:j+1]))
            i = j 

print(Solution().solve([-1,2,5,-7,-2,4]))

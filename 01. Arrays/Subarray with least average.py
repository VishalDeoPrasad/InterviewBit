class Solution:
    def solve(self, A, B):
        least_avg = sum(A[:B])/B
        idx = 0
        for i in range(len(A)-B+1):
            curr_avg = sum(A[i:i+B])/B
            print(curr_avg)
            if curr_avg < least_avg:
                least_avg = curr_avg
                idx = i
        return idx

A = [ 20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11 ]
B = 9
print(Solution().solve(A, B))
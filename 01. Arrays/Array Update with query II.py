class Solution:
    def prefixSum(self, arr):
        pf = []
        pf.append(arr[0])
        for i in range(1, len(arr)):
            pf.append(pf[i-1]+arr[i])
        return pf

    def solve(self, N, queries):
        arr = [0]*N
        for q in queries:
            if q[1] <= N-1:
                arr[q[0]-1] += q[2]
                arr[q[1]] -= q[2]
            else:
                arr[q[0]-1] += q[2]
        
        arr = self.prefixSum(arr)
        return arr
A = 10
B =[[1, 3, 10],
    [6, 9, 2],
    [3, 5, 3],
    [2, 8, 4],
    [6, 7, 5]
]
query = [[4,6,3], [6,9,2], [2,7,-1], [7,9,2]]
print(Solution().solve(A, B))

# 0 1  2 3 4 5 6  7 8 9
# 0 0 -1 0 3 0 2 -1 1 0 
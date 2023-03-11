class Solution:
    def solve(self, A, B):
        row = len(A)
        col = len(A[0])
        i, j = 0, col-1
        min_value = 9999999999
        while i<row and j>=0:
            if A[i][j] == B:
                curr_val = (i+1)*1009 + (j+1)
                if curr_val < min_value:
                    min_value = curr_val
                j -= 1
            elif A[i][j] > B:
                j -= 1
            elif A[i][j] < B:
                i += 1

        if min_value == 9999999999:
            return -1
        else:
            return min_value
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = 2

print(Solution().solve(A,B))
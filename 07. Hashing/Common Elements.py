class Solution:
    def solve(self, A, B):
        value_count = {}
        for i in range(len(A)):
            if A[i] not in value_count:
                value_count[A[i]] = 1
            else:
                value_count[A[i]] += 1
                
        ans = []
        for i in range(len(B)):
            if B[i] in value_count:
                value_count[B[i]] -= 1
                if value_count[B[i]] >= 0:
                    ans.append(B[i])
        return ans
    
A = [1, 2, 2, 1]
B = [2, 3, 1, 2]

print(Solution().solve(A,B))

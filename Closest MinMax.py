class Solution:
    def solve(self, A):
        minn = min(A)
        maxx = max(A)
        min_list = []
        max_list = []
        for i in range(len(A)):
            if A[i] == minn:
                min_list.append(i)
            if A[i] == maxx:
                max_list.append(i)

        ans = 9999999
        for mn in min_list:
            for mx in max_list:
                if abs(mn-mx) < ans:
                    ans = abs(mn-mx)
        return ans+1
    
A = [2, 6, 1, 6, 9]
print(Solution().solve(A))
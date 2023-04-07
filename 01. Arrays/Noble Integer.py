class Solution:
	def solve(self, A):
		A.sort()
		cnt = 0
		for i in range(len(A)):
			if A[i] == i:
				cnt += 1
		return cnt

print(Solution().solve([-2,-1,4,3,2,6]))
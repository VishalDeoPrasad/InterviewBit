class Solution:
	def solve(self, A):
		A.sort(reverse=True)
		idx_arr = [0]
		for i in range(1, len(A)):
			if A[i] == A[i-1]:
				idx_arr.append(idx_arr[i-1])
			else:
				idx_arr.append(i)
		for i in range(len(A)):
			if A[i] == idx_arr[i]:
				return 1
		return -1
	
print(Solution().solve([2,5,4,1,6,9,5,5,3,5,6,7,5,7]))
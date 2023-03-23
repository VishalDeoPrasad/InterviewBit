class Solution:
	def sum_of_ap(self, n, a, d):
		return int((n/2)*(2*a+(n-1)*d))
	
print(Solution().sum_of_ap(5,1,3))
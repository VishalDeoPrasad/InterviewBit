class Solution:
    def missingNumber(self,array,n):
        return (n*(n+1))//2 - sum(array)
    
print(Solution().missingNumber([1,2,3,5], 5))
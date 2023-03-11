class Solution:
	# @param A : integer
	# @return an integer
    def reverse(self, n):
        rev = 0
        while n>0:
            a = n%10
            rev = rev*10 + a 
            n = n//10
        print(rev)
        return rev
        
    def isPalindrome(self, A):
        if A < 0:
            return 0
        return 1 if self.reverse(A) == A else 0

print(Solution().isPalindrome(2147447412))
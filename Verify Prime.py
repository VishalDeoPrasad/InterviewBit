class Solution:
    def isPrime(self, A):
        if A < 2:
            return 0
        
        if A%2 == 0: #Even Division Check
            return 0
            
        for i in range(3, (A**1//2)+1, 2):  #odd Division Check
            if A%i == 0:
                return 0
        return 1
    
print(Solution().isPrime(7))
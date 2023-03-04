class Solution:     
    def gcd(self, A,B):
        n1 = A
        n2 = B
        rem = 0
        while (n1%n2 != 0):
            rem = n1%n2
            n1 = n2
            n2 = rem
        return n2
    
    def lcm(self, A,B):
        gcd = self.gcd(A,B)
        l = (A*B)//gcd
        return l
        
    def solve(self, A, B):
        return self.lcm(A, B)
    
print(Solution().solve(4,6))

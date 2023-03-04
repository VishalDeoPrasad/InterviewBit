class Soluction:
    def gcd1(self, A,B):
        least = 0
        if A > B:
            least = B
        else:
            least = A

        for i in range(least, 1, -1):
            if A%i == 0 and B%i == 0:
                return i
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
        l = (A*B)/gcd
        return l


print(Soluction().gcd(20, 40))
print(Soluction().lcm(3,7))

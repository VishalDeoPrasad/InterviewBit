class Solution:
    def allFactors1(self, A):
        fact = [i for i in range(1, A+1) if A%i == 0]
        return fact

    def allFactors(self, A):
        factors = []
        for i in range(1, int(math.sqrt(A))+1):
            if A % i == 0:
                factors.append(i)
                if i != A // i:
                    factors.append(A // i)
        factors.sort()
        return factors
    
    
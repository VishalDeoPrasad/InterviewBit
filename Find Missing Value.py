class Soluction:
    #idea 1 - Brute Force: check 1 is present check 2 is present and so on until get the missing value
    #TC - O(N*N), SC - O(1)
    def solve1(self, A):
        for i in range(1, len(A)+2):
            if i not in A:
                return i
    #idea 2 - Sum of n number: problem is it can overflow if the value is high
    #TC - O(N), SC - O(1)       
    def solve2(self, A):
        n = len(A)+1
        actual_sum = (n*(n+1))//2
        given_sum = sum(A)
        return actual_sum - given_sum

    #idea 3: Find Using XOR(a^a = 0)
    #TC - O(N), SC - O(1)
    def solve3(self, A):
        a = 0
        n = len(A)+1
        for i in range(1, n+1):
            a = a^i
        
        b = 0
        for i in range(len(A)):
            b = b ^ A[i]

        return a^b


print(Soluction().solve3([3,7,4,8,5,9,2,1]))
print(Soluction().solve2([3,7,4,8,5,9,2,1]))
print(Soluction().solve1([3,7,4,8,5,9,2,1]))
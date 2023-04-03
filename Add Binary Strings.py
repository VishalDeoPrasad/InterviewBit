class Solution:
    def NormalizeString(self, A,B):
        diff = abs(len(A)-len(B))
        if len(A)>len(B):
            B = "0"*diff+B 
        else:
            A = "0"*diff+A 
        return A,B
            
    def addBinary(self, A, B):
        A,B = self.NormalizeString(A,B)
        carry = 0
        ans = ""
        for i in range(len(A)-1, -1, -1):
            summ = carry+int(A[i])+int(B[i])
            ans = str(summ%2) + ans
            carry = summ//2
            if i==0 and carry:
                ans = str(carry)+ans
        return ans
A = "1010010101110"
B = "00101101110"          
print(Solution().addBinary(A,B))
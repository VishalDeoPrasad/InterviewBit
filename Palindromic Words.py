class Solution:
    def Palindrom(self, S):
        pali = ""
        for ch in S:
            pali = ch+pali
        return pali           
    
    def solve(self, A):
        A = A.split(" ")
        cnt = 0
        for st in A:
            if st == self.Palindrom(st):
                cnt += 1
        return cnt
A = "wow mom"
print(Solution().solve(A))
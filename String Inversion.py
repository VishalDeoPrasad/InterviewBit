class Solution:
    def solve(self, A):
        new_A = ""
        for i in range(len(A)):
            if ord(A[i]) >= 65 and ord(A[i]) <= 90:
                new_A += chr(ord(A[i]) + 32)
            else:
                new_A += chr(ord(A[i]) - 32)
        return new_A
    
print(Solution().solve("InterviewBit"))
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A) < 8 or len(A) > 15:
            return 0
        Special_char =['$', '@', '#', '%',"&","*","!"]
        valid = {'upper':0, 'lower':0, 'digit':0, 'special':0 }
        for ch in A:
            if ch.isdigit():
                valid['digit'] = 1
            if ch.isupper():
                valid['upper'] = 1
            if ch.islower():
                valid['lower'] = 1
            if ch in Special_char:
                valid['special'] = 1
        if sum(valid.values()) == 4:
            return 1
        else:
            return 0
            
print(Solution().solve("InterviewBit@1"))
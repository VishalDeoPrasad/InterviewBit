class Solution:
    def solve(self, A):
        alpha_list  = []
        for i in range(97, 123):
            alpha_list.append(A.count(chr(i)))
        return alpha_list

print(Solution().solve("InterviewBit"))
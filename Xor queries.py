class Solution:
    def xor(self,A,s,e):
        ans = 0
        for i in range(s-1, e):
            ans = ans^A[i]
        return ans
    
    def UnsetCount(self,A,s,e):
        cnt = 0
        for i in range(s-1, e):
            if A[i]&1 == 0:
                cnt += 1
        return cnt

    def solve(self, A, B):
        ans = []
        for s,e in B:
            xor_sum = self.xor(A,s,e)
            unset_cnt = self.UnsetCount(A,s,e)
            ans.append([xor_sum, unset_cnt])
        return ans
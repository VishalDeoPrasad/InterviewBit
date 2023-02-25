class Solution:
    def solve(self, A, B, C):
        x=A
        while(x%10!=C):
            x+=1
            
        ans=(B-x)//10+1
        return ans
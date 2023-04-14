class Solution:
    def reverse(self,A,s,e):
        while s<e:
            A[s],A[e] = A[e],A[s]
            s += 1
            e -= 1
        return A
    def strip(self, A):
        for i in range(len(A)):
            if A[i] != " ":
                A = A[i:]
                break 
        for i in range(len(A)-1,-1,-1):
            if A[i] != " ":
                A = A[:i+1]
                break
        return A     

    def solve(self, A):
        A = list(A)
        A = self.reverse(A,0,len(A)-1)
        A.append(" ")
        i,j =0,0
        while j<len(A):
            while A[j] != " ":
                j += 1
            
            A = self.reverse(A,i,j-1)
            j += 1
            i = j
        
        A = "".join(A)
        return A.strip()
        
a = "   a ci f ved pu vkfzbu bnbvlvgkua imjd hrrnx nopp p kso iejgcd wyalgcxie yfslfzzw lygatpbv wr budfobxsm   "
print(Solution().solve(a))

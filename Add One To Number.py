class Solution:
    def removeZeros(self, A):
        i = 0
        while i<len(A)-1:
            if A[i] == 0:
                i += 1
            else:
                break
        return A[i:]
        
    def plusOne(self, A):
        A = self.removeZeros(A)
        idx = len(A)-1              
        while idx >= 0:             
            if A[idx] < 9:          
                A[idx] += 1         
                return A            
            else:
                A[idx] = 0          
                idx -= 1            
                if idx == -1:
                    A.insert(0,1)
                    return A    #[1]+A
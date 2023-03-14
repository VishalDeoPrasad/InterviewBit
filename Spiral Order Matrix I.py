class Solution:
    def boundary(self, A):
        row = len(A)
        col = len(A[0])
        sprial = []
        i, j = 0,0
        while j < col-1:
            sprial.append(A[i][j])
            j += 1

        while i < row-1:
            sprial.append(A[i][j])
            i += 1
        
        while j >  0:
            sprial.append(A[i][j])
            j -= 1
        
        while i >  0:
            sprial.append(A[i][j])
            i -= 1

        return sprial
    def spiralOrder(self, A):
        sprial = []
        for i in range(len(A[0])):
            row = len(A)-i
            col = len(A[0])-i
            temp = self.boundary(A[i:row :i:col])
            sprial.append(temp)
        return sprial

A = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
print(Solution().spiralOrder(A))

#[1, 2, 3, 6, 9, 8, 7, 4, 5]
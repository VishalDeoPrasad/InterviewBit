class Solution:
    def boundary(self, Mat, i, j, M, N):
        bound = []
        for l in range(1, N):
            #print(Mat[i][j], end=" ")
            bound.append(Mat[i][j])
            j += 1
        
        for l in range(1, M):
            #print(Mat[i][j], end=" ")
            bound.append(Mat[i][j])
            i += 1
        
        for l in range(1, N):
            #print(Mat[i][j], end=" ")
            bound.append(Mat[i][j])
            j -= 1
        
        for l in range(1 ,M):
            #print(Mat[i][j], end=" ")
            bound.append(Mat[i][j])
            i -= 1
            
        return bound
    def spiralOrder(self, Mat):
        sprial = []
        M, N = len(Mat), len(Mat[0])
        i,j = 0,0
        while N>1:
            temp = self.boundary(Mat, i, j, M, N)
            sprial.extend(temp)
            M = M-2
            N = N-2
            i = i+1
            j = j+1
        if N == 1:
            #print(Mat[i][j])
            sprial.append(Mat[i][j])
        return sprial
A = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
A2 = [
            [1, 2, 3, 4, 5, 6],
            [4, 5, 6, 7, 8, 9],
            [7, 8, 9, 10,11,12], 
            [11,12,13,14,13,14]
    ]

A3 = [
      [1]
    ]
A4 = [
        [313, 157, 290, 113, 119, 118, 187, 360, 104, 365, 197, 103, 355, 240, 337, 174, 138, 252]
    ]
print(Solution().spiralOrder(A4))
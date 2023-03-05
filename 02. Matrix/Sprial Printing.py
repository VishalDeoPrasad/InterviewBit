class Sprial:
    def boundary(self, Mat):
        M = len(Mat)
        N = len(Mat[0])
        i,j = 0, 0
        for l in range(1, N):
            print(Mat[i][j], end=" ")
            j += 1
        
        for l in range(1, M):
            print(Mat[i][j], end=" ")
            i += 1
        
        for l in range(1, N):
            print(Mat[i][j], end=" ")
            j -= 1
        
        for l in range(1 ,M):
            print(Mat[i][j], end=" ")
            i -= 1
    def printing(self, Mat):
        M = len(Mat)
        N = len(Mat[0])
        i, j = 0, 0
        while N>1:
            self.boundary(Mat)
            print()
            N = N-2
            i += 1
            j += 1
            if N == 1:
                print(Mat[i][j])


mat = [[1,2,3,4],[4,5,6,7],[7,8,9,10], [11,12,13,14]]
mat1 = [[1,2,3,4],[23,5,6,7],[7,8,9,10], [11,12,13,14], [15,16,17,18], [19,20,21,22]]
mat2 = [[1,2,3,4,5,6],[4,5,6,7,8,9],[7,8,9,10,11,12], [11,12,13,14,13,14]]
Sprial().printing(mat)
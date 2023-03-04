class Rotation:
    def Transpose(self, A):
        T = []
        for i in range(len(A[0])):
            temp = []
            for j in range(len(A)):
                temp.append(A[j][i])
            T.append(temp)
        return T
    
    def reverse(self, A):
        n = len(A)
        for i in range(n//2):
            j = n-i-1
            A[i], A[j] = A[j], A[i]
        return A
    
    def degree(self, A):
        print(A)
        T = self.Transpose(A)
        print(T)
        for i in range(len(T)):
            T[i] = self.reverse(T[i])
        print(T)

mat = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]
mat1 = [[1,2,3],[4,5,6],[7,8,9], [10,11,2]]
mat2 = [[1,2],[5,6],[8,9], [11,12]]
# print(mat)
# print(Rotation().Transpose(mat))
print(Rotation().degree(mat))

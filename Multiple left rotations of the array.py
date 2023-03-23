class Solution:
    def rotate(self, A):
        for i in range(len(A)//2):
            j = len(A)-1-i
            A[i], A[j] = A[j], A[i]
        return A
        
    def solve(self, A, B):
        n = len(A)
        A = self.rotate(A)
        mat = []
        for k in B:
            k = k%n
            mat.append(self.rotate(A[:n-k])+self.rotate(A[n-k:]))
        return mat
    
A = [1, 2, 3, 4, 5]
B = [2, 3]
print(Solution().solve(A,B))
class Solution:
    #Idea 1- Brute force 
    #TC - O(N*N) SC = O(N)
    def solve1(self, A, B):
        begger = [0]*A
        for i in range(len(B)):
            start = B[i][0]-1
            end = B[i][1]
            bill = B[i][2]
            for j in range(start, end):
                begger[j] += bill
        return begger
    
    def solve(self, A, B):
        A = [0]*A
        for q in B:
            for i in range(q[0]-1, q[1]):
                A[i] += q[2]
        return A
    
A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]       
print(Solution().solve(A, B))
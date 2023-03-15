class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        pascal = []
        for i in range(A+1):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(pascal[i-1][j-1]+pascal[i-1][j])
            pascal.append(temp)
        return pascal
    
print(Solution().getRow(5))
                    
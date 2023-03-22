class Solution:
    def average(self,A,B,start,end):
        sum = 0
        for i in range(start, end):
            sum += A[i]
        return sum/B
    
    def solve1(self, A, B):
        least_avg = 999999999
        min_idx = 0
        for i in range(len(A)-B+1):
            j = i+B
            temp = self.average(A,B,i,j)
            if least_avg > temp:
                least_avg = temp
                min_idx = i
        return min_idx
    
    def solve(self, A, B):
        least_sum = sum(A[:B])
        axu = []
        axu.append((least_sum, 0, B-1))
        for i in range(B, len(A)):
            least_sum = least_sum+A[i]-A[i-B]
            axu.append((least_sum,i-B+1, i))
        
        avg = axu[0][0]/B
        idx = axu[0][1]
        for i in range(1, len(axu)):
            if axu[i][0]/B < avg:
                avg = axu[i][0]/B
                idx = axu[i][1]
        return idx

        






A1=[3, 7, 90, 20, 10, 50, 40]
B1=3

A2=[3, 7, 5, 20, -10, 0, 12]
B2=2

print(Solution().solve(A1, B1))
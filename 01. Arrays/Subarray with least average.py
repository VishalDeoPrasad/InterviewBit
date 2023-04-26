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
            print(least_sum, end = " ")
            axu.append((least_sum,i-B+1, i))
        
        avg = axu[0][0]/B
        idx = axu[0][1]
        for i in range(1, len(axu)):
            if axu[i][0]/B < avg:
                avg = axu[i][0]/B
                idx = axu[i][1]
        return idx,avg
    
    def solve1(self, A, B):
        next_sum = sum(A[:B])
        idx = 0
        min_avg = next_sum/B
        for i in range(B, len(A)):
            next_sum = next_sum + A[i] - A[i-B]
            print(next_sum, end=" ")
            if min_avg > next_sum/B:
                min_avg = next_sum/B
                idx = i-B+1
        
        return idx, min_avg

A = [ 18, 11, 16, 19, 11, 9, 8, 15, 3, 10, 9, 20, 1, 19 ]
B = 1

A1=[3, 7, 90, 20, 10, 50, 40]
B1=3

A2=[3, 7, 5, 20, -10, 0, 12]
B2=2

A3 =[ 15, 7, 11, 7, 9, 8, 18, 1, 16, 18, 6, 1, 1, 4, 18 ]
B3 = 6

print(Solution().solve(A3, B3))
print(Solution().solve1(A3, B3))
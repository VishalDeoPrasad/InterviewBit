class Solution:
    def solve(self, A):
        cnt = 0
        for i in range(3, A+1):
            if i == 4:
                continue
            if i%2 == 0: #even
                a = (i//2)**2
                b = a-1
                c = a+1
                print(i,b,c)
                if i <= A and b <= A and c <= A:
                    cnt += 1
                
            elif i%2 != 0: #odd
                a = i**2
                b = a//2
                c = a//2+1
                print(i,b,c)
                if i <= A and b <= A and c <= A:
                    cnt += 1
        return cnt
    
print(Solution().solve(5))

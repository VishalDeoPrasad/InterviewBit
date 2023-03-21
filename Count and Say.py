class Solution:
    def count(self, A):
        string = ""
        cnt = 1
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                cnt += 1
            else:
                string += str(cnt)
                string += A[i]
                cnt = 1
            if i == len(A)-2:
                    string += str(cnt)
                    string += A[i+1]
        return string
    def countAndSay(self, A):
        if A == 1:
            return 1
        temp = "11"
        for i in range(2, A):
            temp = self.count(temp)
        return temp
            
print(Solution().countAndSay(5)) 
				
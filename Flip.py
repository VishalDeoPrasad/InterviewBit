class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        bit = []
        flag = True
        for i in range(len(A)):
            if A[i] == "0":
                bit.append(1)
                flag = False
            else:
                bit.append(-1)
                
        if flag:
            return []
        
        #Apply Kadana Alog
        curr_sum = 0
        max_sum = 0
        left, right = 0,0
        l = 0
        for i in range(len(bit)):
            curr_sum += bit[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
                right = i
                left = l
            if curr_sum < 0:
                curr_sum = 0
                l = i+1

        return [left+1, right+1]


A = [1,0,1,1,0,0,0,1,0,1]
A1 = [0,1,0]
print(Solution().flip(A1))
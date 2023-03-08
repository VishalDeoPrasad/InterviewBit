class Solution:
    def majorityElement(self, A):
        cnt_dic = {}
        for i in range(len(A)):
            if A[i] not in cnt_dic:
                cnt_dic[A[i]] = 1
            else:
                cnt_dic[A[i]] = cnt_dic[A[i]]+1
        
        for key,val in cnt_dic.items():
            if val > len(A)/2:
                return key

print(Solution().majorityElement([2,1,2]))
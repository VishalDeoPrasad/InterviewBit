class Solution:
    def majorityElement(self, A):
        dic = {}
        for i in range(len(A)):
            if A[i] not in dic:
                dic[A[i]] = 1
            else:
                dic[A[i]] = dic[A[i]] + 1
        n = len(A)
        for key, val in dic.items():
            if val > n/2:
                return key
        return 0

print(Solution().majorityElement([2,1,2]))

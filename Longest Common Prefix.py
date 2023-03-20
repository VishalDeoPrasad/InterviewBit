class Solution:
    #Idea 1 - Brute force 
    def longestCommonPrefix1(self, A):
        min_len = len(A[0])
        min_str = A[0]
        for strr in A:
            if len(strr) < min_len:
                min_len = len(strr)
                min_str = strr
        comm = ""
        for  ch in min_str:
            for i in range(len(min_str)):
                cnt = 0
                for j in range(len(A)):
                    if A[j][i] != ch:
                        break
                    else:
                        cnt += 1
                        if cnt == len(A):
                            comm += ch
        print(min_str)
        return comm
    
    #idea 2 - sort and compair first and last element
    #TC - O(N) SC - O(1)
    def longestCommonPrefix(self, A):
        A.sort()
        first = A[0]
        last = A[len(A)-1]
        minn = ""
        if len(first) > len(last):
            minn = last
        else:
            minn = first
        
        comm = ""   
        for i in range(len(minn)):
            if first[i] == last[i]:
                comm += first[i]
        return comm
    
A =  [ "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
      "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaa", 
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
      "aaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", 
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" ]        
       
#A = ["abcdefgh", "abghijk", "abcef"]
print(Solution().longestCommonPrefix(A)) 
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        dict = {}
        for ch in A:
            if ch not in dict:
                dict[ch] = 1
            else:
                dict[ch] += 1
        for key, val in dict.items():
            cnt = 0
            print(key, val)
            if val%2 == 1:
                cnt += 1
        print(cnt)
                
    
print(Solution().solve("aaabbbc"))
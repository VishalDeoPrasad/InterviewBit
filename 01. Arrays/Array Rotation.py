class Solution:
    def rotateArray(self, a, b):
        ret = []
        for i in range(len(a)):
            ret.append(a[(i + b) % len(a)])
        return ret

print(Solution().rotateArray([3,6,9,8,7,4], 3)) 
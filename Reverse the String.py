class Solution:
    def solve1(self, A):
        A_ = A.split()
        n = len(A_)
        for i in range(n//2):
            j = n-i-1
            A_[i], A_[j] = A_[j], A_[i] 
        A_ = " ".join(word for word in A_)
        return A_

    def solve(self, A):
        print(A)
        #' '.join(A.strip().split(' ')[::-1])
        print(" ".join(A.strip().split(' ')[::-1]))

print(Solution().solve("The Sky is Blue"))
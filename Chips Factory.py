class Solution:
    def solve1(self, A):
        for i in range(len(A)):
            if A[i] == 0:
                A.remove(A[i])
                A.append(0)
        return A

    def solve(self, A):
        new_A = [num for num in A if num]
        new_A += [0]*(len(A)-len(new_A))
        return new_A
A = [0, 1, 2, 3]
print(Solution().solve(A))

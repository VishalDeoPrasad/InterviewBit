class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        A.sort()
        q1 = len(A)//3
        q2 = q1*2
        if A[q1] == A[q2]:
            return A[q1]
        else:
            if A.count(A[q1]) > len(A)//3:
                return A[q1]
            elif A.count(A[q2]) > len(A)//3:
                return A[q2]
            elif A.count(A[q2+1]) > len(A)//3:
                return A[q2+1]
        return -1
A = [ 1000371, 1000110, 1000945, 1000945, 1000321, 1000593, 1000945, 1000877, 1000768, 1000708, 1000853, 1000945, 1000945, 1000238, 1000059, 1000446, 1000945, 1000329, 1000945, 1000247 ]
print(Solution().repeatedNumber(A))
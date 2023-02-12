#Given n array elements, check if there exists a pair(i, j) such that ar[i]+ar[k]=k and i != j.
def pairSum(ar, key):
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i==j:
            if ar[i]+ar[j] == key:
                return (i,j)
    return 0

test_cases = [[9,5,9,7,4,5,5,7]]
for t in test_cases:
    print(pairSum(t, 10))

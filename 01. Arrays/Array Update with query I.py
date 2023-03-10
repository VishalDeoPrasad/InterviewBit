#Given N array elements initialized with 0.
def prefixSum(arr):
    pf = []
    pf.append(arr[0])
    for i in range(1, len(arr)):
        pf.append(pf[i-1]+arr[i])
    return pf

def ArrayUpdate(N,query):
    arr = [0]*N
    for q in query:
        arr[q[0]] = q[1]
    print(arr)
    arr = prefixSum(arr)
    return arr



query = [[4,3], [6,2], [2,-1], [7,2]]
print(ArrayUpdate(10, query))
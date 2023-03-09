#Given N array elements initialized with 0.
def ArrayUpdate(N,query):
    arr = [0]*N
    for q in query:
        arr[q[0]] = q[1]
    return arr



query = [[4,3], [6,2], [3,-1], [7,2]]
print(ArrayUpdate(10, query))
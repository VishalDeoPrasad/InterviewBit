def CostEastimator(arr):
    cost = 0
    arr.sort(reverse=True)
    for i in range(len(arr)):
        cost += arr[i]*(i+1)
    return cost

print(CostEastimator([1,6,4]))
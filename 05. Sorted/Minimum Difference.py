def Minimum_Difference(arr):
    arr.sort()
    ans = 999999999
    for i in range(1, len(arr)):
        ans = min(ans, arr[i]-arr[i-1])
    return ans

print(Minimum_Difference([2,4,6,8,10,11]))
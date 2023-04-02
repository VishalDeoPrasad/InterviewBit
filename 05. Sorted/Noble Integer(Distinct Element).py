def NobleInteger(arr):
    cnt = 0
    arr.sort()
    for i in range(len(arr)):
        if arr[i] == i:
            cnt += 1
    return cnt

print(NobleInteger([1,-5,3,5,-10,4]))
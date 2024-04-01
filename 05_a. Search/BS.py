def binary_search(arr, key):
    arr.sort()
    left = 0
    right = len(arr)-1
    mid = 0
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == key:
            return "Key Matched:",mid
        elif arr[mid] > key:
            right = mid-1
        else:
            left = mid+1
    return "key didn't match"

arr = [1,2,2,3,4,5,6,7,8,8,9]
print(binary_search(arr, 8))
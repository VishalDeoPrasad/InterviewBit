def binarySearch(lst, key):
    mid = 0
    left, right = 0, len(lst)-1
    while left <= right:
        mid = (left+right)//2
        if lst[mid] == key:
            return mid
        elif key > lst[mid]:
            left = mid+1
        elif key < lst[mid]:
            right = mid-1
    return -1
            
print(binarySearch([1,2,3,4,5,6,7,8,9], 10))
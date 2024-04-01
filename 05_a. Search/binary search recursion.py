def binary_search(lst, key, left, right):
    #base case 1: if start index greater the end index
    if left > right:
        return -1
    
    #base case 2: if element found return index
    mid = (left+right)//2
    
    if lst[mid] == key:
        return mid
    if key > lst[mid]:
        return binary_search(lst, key, mid+1, right)
    elif key < lst[mid]:
        return binary_search(lst, key, left, mid-1)

    
lst = [1,2,3,4,5,6,7,8,9]
key = 3
ans = binary_search(lst, key, 0, len(lst)-1)
print(ans)
    
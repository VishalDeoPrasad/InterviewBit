def subArray(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            print(arr[i:j], end="  ")
    print()
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print([i,j], end="  ")
    
    return (len(arr)*(len(arr)+1))/2

print(subArray([1,2,3,4,5]))
def rotation(arr):
    n = len(arr)
    for i in range(n//2):
        j = n-i-1
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def Right2Left(arr, k):
    arr =  rotation(arr)
    arr = rotation(arr[:k]) + rotation(arr[k:])
    return arr

ar = [1,2,3,4,5,6,7,8,9]
k = 5
print(Right2Left(ar, k))

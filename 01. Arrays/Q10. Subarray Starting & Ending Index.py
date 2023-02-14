def Subarray(arr, k):
    n = len(arr)
    print("Total Subarray of size k =",n-k+1)
    for i in range(n-k+1): #add +1 because of it will not takes last
        j = i+k
        print((i,j), end="  ")
        print(arr[i:j])

print(Subarray([1,2,3,4,5,6,7,8,9], 3))
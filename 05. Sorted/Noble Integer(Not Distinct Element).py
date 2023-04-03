#idea 1 - Using Aux array 
#TC - O(NlogN) SC - O(N) 
def NobleInteger(arr):
    arr.sort()
    count = [0]*len(arr)
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            count[i] = i
        else:
            count[i] = count[i-1]
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == count[i]:
            cnt += 1

    return cnt

#idea 2 - without Aux array 
#TC - O(NlogN) SC - O(1) 


print(NobleInteger([-10,5,4,7,1,1,1]))
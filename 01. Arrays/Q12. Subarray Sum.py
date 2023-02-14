# Python way
def SubarraySum(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            print((i,j), end="  ")
            print(sum(arr[i:j+1]), end="  ")
            print(arr[i:j+1])
    
#SubarraySum([1,2,3,4,5])

#In More General Way - Time complexity : O(n*n*n)
def sum_fun(arr, start, end, how=0):
    if how == 0:
        sumi = 0
        for i in range(start, end+1):
            sumi += arr[i]
        return sumi
    return sum(arr[start:end+1])

def sub_print(arr, start, end, how=0):
    if how == 0:
        temp_lst = []
        for i in range(start, end+1):
            temp_lst.append(arr[i])
        return temp_lst
    else:
        return arr[start:end+1]

def Subarray_Sum(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            print((i,j), end="  ")
            print(sum_fun(arr,i,j), end="  ")
            print(sub_print(arr,i,j))
    
Subarray_Sum([1,2,3,4,5])

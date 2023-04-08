#Q. Given an array of size N check if threr exist a subarray with sum=0

def MinimumSum(arr):
    aux = []
    aux.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == 0:
            return True
        summ = aux[i-1]+arr[i]
        if summ == 0:
            return True
        aux.append(aux[i-1]+arr[i])
        
    return aux

print(MinimumSum([2,5,4,8,2,3,5,-10]))

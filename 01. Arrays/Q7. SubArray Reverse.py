#Given an array and start index and end index reverse entire subarray.
def reversArray(arr):
    n = len(arr)
    for i in range(n//2):
        j = n-i-1
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def SubarrayReverse(arr, si, ei):
    return arr[:si]+reversArray(arr[si:ei+1])+ar[ei+1:]

ar = [1,2,3,4,5,6,7,8,9,10]
si = 4
ei = 8
print(SubarrayReverse(ar, si, ei))
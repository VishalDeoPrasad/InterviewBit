#find the number of subarray that can be of length of k using the given array
def subArray(ar, size):
    return len(ar) - size + 1

print(subArray([1,2,3,4,5,6], 4))

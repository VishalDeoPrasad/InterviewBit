#Find the max subarray sum with the length k.
def solve(arr, k):
    n = len(arr)
    max_sum = 0
    for i in range(n-k+1):
        j = i+k
        if sum(arr[i:j]) > max_sum:
            max_sum = sum(arr[i:j])
    return max_sum

print(solve([1,2,3,4,5], 3))


#Given N array element print all subarray sum of size k.
def solve(arr, k):
    n = len(arr)
    sliding_sum = []
    last_sum = arr[0]
    for i in range(1, n-k+1):

        

#Given N array elements, reverse entire string
def reverse(arr):
    n = len(arr)
    for i in range(n//2):
        j = n-i-1
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr

test_cases = [[5,6,9,8,7,8], [5,4,9,6,7]]
for t in test_cases:
    print(reverse(t)) 
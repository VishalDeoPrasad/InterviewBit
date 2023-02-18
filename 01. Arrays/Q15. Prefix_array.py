# Q. Given an array and and n-query find the sum of all element from L-R.
def elementSum(arr):
    sum_list = []
    sum_list.append(arr[0])
    for i in range(1, len(arr)):
        sum_list.append(sum_list[i-1]+arr[i])

    return sum_list

carry_sum = elementSum([1,2,3,4,5,6,7,8,9])
query = [(4,7), (3, 8), (1,6), (3,5), (0,8)]
for q in query:
    if q[0] == 0:
        print(carry_sum[q[1]])
    else:
        print(carry_sum[q[1]]-carry_sum[q[0]-1])

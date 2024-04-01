def function(A, B):
    prefix_sum = []
    prefix_sum.append(sum(A[:B]))

    for i in range(1, len(A)-B+1):  # Adjusted loop range
        add = prefix_sum[-1] - A[i-1] + A[i+B-1]  # Changed index to access the last element in prefix_sum
        prefix_sum.append(add)

    return prefix_sum

A = [3, 7, 90, 20, 10, 50, 40]
B = 3
ans = function(A, B)
print(ans)
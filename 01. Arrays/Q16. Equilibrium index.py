# Q.Given an array element count number of equlibrium index. an index i is said to be equilibrium index if sum of all element
# before ith index is equal to sum of all element after ith index.

def prefixArray(arr):
    prefix_arr = []
    prefix_arr.append(arr[0])
    for i in range(1, len(arr)):
        prefix_arr.append(prefix_arr[i-1]+arr[i])
    return prefix_arr

def EquilibriumIndex(arr):
    n = len(arr)
    pf = prefixArray(arr)
    print(pf)
    cnt = 0
    lst = []
    for i in range(n):
        if i == 0:
            if pf[n-1]-pf[i+1] == 0:
                cnt += 1
                lst.append(i)
        elif pf[i-1] == pf[n-1]-pf[i]:
            cnt += 1
            lst.append(i)
    print(lst)
    return cnt
print(EquilibriumIndex([-7,1,5,2,-4,3,0]))
    
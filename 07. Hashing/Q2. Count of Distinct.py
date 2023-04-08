def ArrayFrequency(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1

    return len(dic)
        



arr = [1,5,8,4,5,2,4,5,4]
query = [2,5,8,4]
print(ArrayFrequency(arr))
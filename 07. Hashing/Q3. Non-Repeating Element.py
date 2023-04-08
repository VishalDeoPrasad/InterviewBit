def ArrayFrequency(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1
    cnt = 0
    for key,val in dic.items():
        if val == 1:
            cnt += 1

    return cnt


arr = [1,5,8,4,5,2,4,5,4]
print(ArrayFrequency(arr))
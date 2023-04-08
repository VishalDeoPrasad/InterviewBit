#Q. Given an array of size "N" and "Q" Queries for every query a number "X" is provided give return the frequency of 'x' in an array:

def ArrayFrequency(arr, query):
    dic = {}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1

    for q in query:
        print(dic[q])
        



arr = [1,5,8,4,5,2,4,5,4]
query = [2,5,8,4]
print(ArrayFrequency(arr, query))
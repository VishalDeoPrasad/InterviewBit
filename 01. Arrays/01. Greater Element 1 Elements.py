#Given N array elements count number of elements having atlest 1 element greater than itself.

#Approch 1: Brute Force Method iterate all element one by one and compair to each and every element.
#Solved in O(n*n)
def LeaderElement(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
                break
    return cnt
t1 = [9,5,7,4,8,9]
t2 = [5,5,5,5,5]
t3 = []
#print(LeaderElement(t3))

#Approch 2: Find max and count the number of max and return length of arr-count of max.
def LeaderElement(arr):
    if len(arr) == 0:
        return 0
    cnt = arr.count(max(arr))
    return len(arr) - cnt

t1 = [10,5,7,4,8,9]
t2 = [5,5,5,5,5]
t3 = []
#print(LeaderElement(t1))

#Approch 3: Find Count max element find the number of occurence of max element without using any function and library
#Time Complexity - O(n+n)
def max_element(arr):
    max_elm = arr[0]
    for a in arr:
        if max_elm < a:
            max_elm = a
    return max_elm

def count_element(arr, num):
    cnt = 0
    for a in arr:
        if num == a:
            cnt += 1
    return cnt

def LeaderElement(arr):
    if len(arr) == 0:
        return 0
    return len(arr) - count_element(arr, max_element(arr))
    
test_cases = [[10,5,7,1,8,9,9], [5,5,5,5,5], []]
#for t in test_cases:
    #print(LeaderElement(t))

#Approch 4: find max and count max element at a sametime and return (lenght of arr - max count)
#Time Complexity - order 
def LeaderElement(arr):
    if len(arr) == 0: return 0
    cnt_max = 1
    max_elm = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == max_elm:
            cnt_max += 1
        elif arr[i] > max_elm:
            max_elm = arr[i]
            cnt_max = 1         
    return len(arr) - cnt_max

test_cases = [[2,8,7,10,7,1,5,10], [10,5,7,4,8,9], [5,5,5,5,5], []]
for t in test_cases:
    print(LeaderElement(t))

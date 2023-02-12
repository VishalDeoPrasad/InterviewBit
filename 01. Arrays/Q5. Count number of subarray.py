#count number of substring that can be generate with the arr.

def substringCount(arr):
    return (len(arr)*(len(arr)+1))//2

print(substringCount([1,2,3,4]))

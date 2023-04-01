def BinaryConversion(n):
    ans = ""
    while n>0:
        a = n%2
        ans = str(a)+ans
        n = n//2
    return ans

print(BinaryConversion(6))
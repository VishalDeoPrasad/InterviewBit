def Pow(a,n):
    if n==0: 
        return 1
    return a*Pow(a, n-1)

print(Pow(2,3))
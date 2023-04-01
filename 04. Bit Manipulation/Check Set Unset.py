#Q. Given N and i, check ith bit of N is set or unset.

def SetUnset(N,i):
    ans = (N>>i) & 1
    return ans

print(SetUnset(6,1))
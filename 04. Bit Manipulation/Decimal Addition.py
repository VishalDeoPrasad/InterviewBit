def normalizeValue(A,B):
    d = abs(len(A)-len(B))
    if len(A) > len(B):
        B = "0"*d+B
    else:
        A = "0"*d+A
    return A,B
def DecimalAddition(A,B):
    A,B = normalizeValue(A,B)
    ans = ""
    carry = 0
    for i in range(len(A)-1,-1,-1):
        sum = carry+int(A[i])+int(B[i])
        base = sum%10
        ans = str(base)+ans
        carry = sum//10
        if i == 0:
            if carry:
                ans = str(carry)+ans
    print("Actural:",int(A)+int(B))
    return ans


print(DecimalAddition("2456458","8764"))
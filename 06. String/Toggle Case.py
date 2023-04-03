def CaseToggle1(S):
    res = ""
    for i in range(len(S)):
        if S[i] >= "a" and S[i] <= "z":
            res += chr(ord(S[i])-32)
        else:
            res += chr(ord(S[i])+32)
    return res

def CaseToggle(S):
    res = ""
    for i in range(len(S)):
        res += chr(ord(S[i])^32)
    return res

print(CaseToggle("aBCdEfG"))
print(CaseToggle1("aBCdEfG"))
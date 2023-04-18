def DigitSum(N):
    if N==0:
        return 0
    return N%10+DigitSum(N//10)

print(DigitSum(1234))
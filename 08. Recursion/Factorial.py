def RecursionFact(N):
    if N==1:
        return 1
    return RecursionFact(N-1)*N

print(RecursionFact(4))
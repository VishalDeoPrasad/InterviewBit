def RecursionSum(N):
    if N == 1:
        return 1
    return RecursionSum(N-1)+N

print(RecursionSum(10))
def RecursionFibonacci(N):
    if N==1 or N==0:
        return 1
    return RecursionFibonacci(N-1)+RecursionFibonacci(N-2)

print(RecursionFibonacci(5))
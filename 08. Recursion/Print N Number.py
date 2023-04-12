def PrintN(N):
    if N==1:
        print(1)
        return
    PrintN(N-1)
    print(N)

PrintN(5)
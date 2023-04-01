#Q. Given +ve Integer N, Find least significant set bit position:

def SetBitPos(N):
    for i in range(32):
        if N>>i & 1 == 1:
            return i

print(SetBitPos(16))
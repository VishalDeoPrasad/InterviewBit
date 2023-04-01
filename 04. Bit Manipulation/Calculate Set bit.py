#@Given Integer N, Calculate no of set bit are there?

#Idea - 1, TC - O(N), SC - O(1)
def CalculateSetBit1(N):
    cnt = 0
    for i in range(31):
        if N>>i & 1 == 1:
            cnt += 1
    return cnt

#Idea - 1, TC - O(log N), SC - O(1)
def CalculateSetBit2(N):
    cnt = 0
    while N>0:
        a = N&1
        cnt += a
        N = N>>1
    return cnt

print(CalculateSetBit1(19)) 
print(CalculateSetBit2(19)) 
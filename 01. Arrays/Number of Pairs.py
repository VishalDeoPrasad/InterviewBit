#Given a string calculate number of pairs i,j such that i<j && s[i] == 'a' && s[j] == 'g':

#idea 1 - Brute force
#TC - O(N*N) SC - O(1)
def StringPair1(s):
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == 'a':
            for j in range(i+1, len(s)):
                if s[j] == 'g':
                    cnt += 1
    return cnt

#idea 2 - Carry backward
#TC - O(N) SC - O(1)
def StringPair2(s):
    cnt = 0
    pair = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == 'g':
            cnt += 1
        elif s[i] == 'a':
            pair += cnt
    return pair

#idea 3 - Carry forward
#TC - O(N) SC - O(1)
def StringPair3(s):
    cnt = 0
    pair = 0
    for i in range(len(s)):
        if s[i] == 'a':
            cnt += 1
        elif s[i] == 'g':
            pair += cnt
    return pair


s = 'abcgaggadfdfgg'
print(StringPair1(s))
print(StringPair2(s))
print(StringPair3(s))

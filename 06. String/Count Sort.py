#TC - O(N) SC - O(1)
def CountSort(S):
    alpha_index = [0]*26
    for i in range(len(S)):
        idx = ord(S[i])-97
        alpha_index[idx] += 1

    res = ""
    for i in range(len(alpha_index)):
        res += alpha_index[i]*chr(i+97)
    return res

print(CountSort("babcdaaefd"))
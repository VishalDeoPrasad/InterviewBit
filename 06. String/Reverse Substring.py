def ReverseSubstring(s, start, end):
    s = list(s)
    for i in range(len(s)):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    return "".join(s)

print(ReverseSubstring("abcdefgh", 2, 5))
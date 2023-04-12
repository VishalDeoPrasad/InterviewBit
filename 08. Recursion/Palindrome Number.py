def Palindrome(word, s, e):
    if s>e:
        return True
    if word[s] == word[e]:
        return Palindrome(word, s+1, e-1)
    
    return False
word = "mallam"
print(Palindrome(word, 0, len(word)-1))
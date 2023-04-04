class Solution:
    def reverse(self, sent, i, j):
        while i < j:
            sent[i], sent[j] = sent[j], sent[i]
            i += 1
            j -= 1
        return sent

    def Reverse_Words(self, sent):
        words = list(sent)
        words = self.reverse(words, i=0, j=len(words)-1)
        s = 0
        for i in range(len(words)):
            if words[i] == " ":
                words = self.reverse(words, s, i-1)
                s = i+1
            if i == len(words)-1:
                words = self.reverse(words, s, i)
        return "".join(words)
        
sentence = "mailmen bring letters"       
print(Solution().Reverse_Words(sentence))
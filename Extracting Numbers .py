class Solution:
    def solve(self, A):
        num = ""
        for ch in A:
            if ch.isnumeric():
                num += ch
            else:
                num += " "
        num = num.split()
        total = 0
        for n in num:
            total += int(n)
        
        return total
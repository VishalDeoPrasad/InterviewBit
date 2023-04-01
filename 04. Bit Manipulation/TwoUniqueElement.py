#Q. Given N array element where every element repect twice except 2 (uniqe Element) find the two unique Element:
class BitManipulation:
    def SetBitPos(self, N):
        for i in range(31):
            if N>>i & 1 == 1:
                return i
            
    def CheckBit(self, N, i):
        return N>>i & 1

    def UniqueElement(self, arr):
        a=0
        left = 0
        right = 0
        for i in range(len(arr)):
            a = a^arr[i]

        set_pos = self.SetBitPos(a)

        for i in range(len(arr)):
            if self.CheckBit(arr[i], set_pos):
                left = left^arr[i]
            else:
                right = right^arr[i]
            
        return left, right

print(BitManipulation().UniqueElement([1,1,2,2,3,3,4,4,5,5,6,6,7,8,8,9]))

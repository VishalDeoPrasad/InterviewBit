class Solution:
    #Idea 1 - Brute force 
    #TC - O(N*N), SC - O(1)
    def solve1(self, arr):
        max_profit = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]-arr[i] > max_profit:
                    max_profit = arr[j]-arr[i]
        return max_profit
    
    #Idea 2 - Auxilary array
    #TC - O(N), SC - O(N)
    def solve2(self,arr):
        aux = [0]*len(arr)
        aux[len(arr)-1] = arr[len(arr)-1]
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > aux[i+1]:
                aux[i] = arr[i]
            else:
                aux[i] = aux[i+1]

        max_profit = 0
        for i in range(len(arr)):
            if aux[i]-arr[i] > max_profit:
                max_profit = aux[i]-arr[i]
        return max_profit 

    #Idea 3 - Buy and sell every data
    #TC - O(N), SC - O(1)
    def solve3(self, arr):
        min_so_far = arr[0]
        max_profit = 0
        for i in range(len(arr)):
            if arr[i] < min_so_far:
                min_so_far = arr[i]
            if arr[i]-min_so_far > max_profit:
                max_profit = arr[i]-min_so_far
        return max_profit
    
    def solve4(self, arr):
        min_so_far = arr[0]
        max_profit = 0
        for i in range(len(arr)):
            min_so_far = min(min_so_far, arr[i])
            max_profit = max(arr[i]-min_so_far, max_profit)
        return max_profit

print(Solution().solve4([3,1,4,8,7,2,7]))


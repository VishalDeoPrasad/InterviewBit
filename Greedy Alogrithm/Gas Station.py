class Solution:
    def canCompleteCircuit1(self, A, B):
        if sum(A) < sum(B):
            return -1
        remaining_fuel = 0
        idx = 0
        for i in range(len(A)):
            remaining_fuel +=  A[i]-B[i]
            if remaining_fuel < 0:
                idx += i+1
                remaining_fuel = 0
        return idx
    

    def canCompleteCircuit(self, A, B):
        if sum(A) < sum(B): return -1
        
        idx = 0
        total_cost = 0
        rem_fuel = 0
        for i in range(len(A)):
            total_cost += A[i]-B[i]
            rem_fuel += A[i]-B[i]
            if rem_fuel < 0:
                idx = i+1
                rem_fuel = 0
        return -1 if total_cost < 0 else idx
        
A = [1, 2, 4]
B = [2, 1, 3]
print(Solution().canCompleteCircuit(A,B))
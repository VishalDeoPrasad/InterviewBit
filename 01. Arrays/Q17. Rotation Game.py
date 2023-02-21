def rotation(arr):
    n = len(arr)
    for i in range(n//2):
        j = n-i-1
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def main():
    a = list(map(int,input().split()))
    N = a[0]
    B = int(input())
    A = a[1:]
    B = B%N #normalize the B
    #rotated_A = A[-B:]+A[:-B]
    rotated_A = rotation(A)
    rotated_A = rotation(A[:B]) + rotation(A[B:])
    for a in rotated_A:
        print(a, end=" ")
    return 0

if __name__ == '__main__':
    main()
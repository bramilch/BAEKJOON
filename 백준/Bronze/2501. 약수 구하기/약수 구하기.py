import sys

input_func = sys.stdin.readline

N, K = map(int, input_func().split())

arr = []
# 6 3
# [1, 2, 3, 6] 

for i in range(1, int(N**(1/2)) + 1):
        if N % i == 0:
                arr.append(i)
                if i < N // i:
                        arr.append(N // i)
                        
arr.sort()

if len(arr) < K:
        print(0)

else:
        print(arr[K-1])
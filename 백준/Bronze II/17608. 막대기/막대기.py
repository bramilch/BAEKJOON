import sys

input_func = sys.stdin.readline

n = int(input_func())
stack = []

for _ in range(n):
    stack.append(int(input_func()))    

right = stack.pop()
count = 1

for i in stack[::-1]:
    if i > right:
        right = i
        count += 1
        
print(count)
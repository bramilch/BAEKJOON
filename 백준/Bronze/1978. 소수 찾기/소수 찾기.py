import sys

input_func = sys.stdin.readline

num = int(input_func())
case = list(map(int, input_func().split())) 

count = 0

for number in case:
        if number > 1:
                for i in range(2, number):
                        if number % i == 0:
                                break
                else:
                        count += 1

print(count)
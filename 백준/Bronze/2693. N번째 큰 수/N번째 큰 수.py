import sys

input_func = sys.stdin.readline

T = int(input_func())
case_dict = {}

for i in range(T):
    case = list(map(int, input_func().split()))
    case_dict[i] = sorted(case, reverse = True)

for j in range(T):
    print(case_dict[j][2])
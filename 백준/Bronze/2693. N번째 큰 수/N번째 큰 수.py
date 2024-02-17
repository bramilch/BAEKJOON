import sys

input_func = sys.stdin.readline

T = int(input_func())
case_dict = {}

for i in range(T):
    case = list(map(int, input_func().split()))
    case_dict[i] = sorted(case, reverse = True)
    print(case_dict[i][2])
def solution(numbers):
    answer = ''
    str_list = []
    
    for i in numbers:
        str_list.append(str(i))
    
    str_list.sort(key = lambda x: x * 3, reverse = True)
    answer = str(int(''.join(i for i in str_list)))
    
    return answer
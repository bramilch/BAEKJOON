def solution(n, left, right):
        # 123 223 333
        # 012 345 678
    answer = []
        
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
        
    return answer

#     answer = []
#     original = []
#     total = []
    
#     #1. 기본 배열 만들기
#     for i in range(1, n + 1):
#         original.append(i) # [1, 2, 3, 4, 5]
    
#     #2. 기본 배열의 인덱싱, 슬라이싱 활용해서 반복 리스트 더해주기
#     for j in range(n):
#         total += [original[j]] * j + original[j : len(original)]       
    
#     #3. left, right로 슬라이싱하기
#     answer = total[left : right + 1]
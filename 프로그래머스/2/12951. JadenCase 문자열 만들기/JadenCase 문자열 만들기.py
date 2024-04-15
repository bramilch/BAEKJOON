def solution(s):
    answer = ''
    s_split = s.split(' ')
    cap = []

    for i in range(len(s_split)):
        cap.append(s_split[i].capitalize())

    answer = ' '.join(cap)
        
    return answer
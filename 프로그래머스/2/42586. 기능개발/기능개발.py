def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0
    
    # O(1)
    while len(progresses) > 0: # pop 되어서 lenth가 0될 때까지 계속 진행
        
        if progresses[0] + speeds[0] * days >= 100: # days는 계속 증가하여 stack 다음 값도 해당하는 days로 바로 계산하여 다 count
            count += 1
            progresses.pop(0)
            speeds.pop(0)
            
        else:
            if count > 0: # 해당하는 days에 100 넘는 count가 > 0 이라면 count 총합을 answer에 append한 후 count 초기화
                answer.append(count)
                count = 0
            else:
                days += 1
            
    answer.append(count)
    
    return answer
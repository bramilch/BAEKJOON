def solution(begin, target, words):
    answer = 0
    queue = []
    
    # BFS 시작점
    queue.append((begin, 0))
    
    # words에 target 없을 경우 0 return
    if target not in words:
        return 0
    
    # 변환된 것과 다음 word 비교
    while queue:
        now, step = queue.pop(0)    
        
        if now == target:
                return step
            
        for word in words:
            count = 0
            
            for i in range(len(word)):
                if now[i] != word[i]:
                    count += 1
            
            # 변환의 의미, 하나만 다를 경우 queue에 step + 1해서 추가
            if count == 1:
                queue.append((word, step + 1))
    
    return answer
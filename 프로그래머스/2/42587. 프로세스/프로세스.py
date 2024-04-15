def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]
    
    while queue:
        idx, priority = queue.pop(0)
        
        if any(priority < q[1] for q in queue):
            queue.append((idx, priority))
            
        else: 
            answer += 1
            
            if location == idx:
                return answer

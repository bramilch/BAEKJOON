def solution(n, computers):
    answer = 0
    queue = []
    visited = [0] * n
    
    # BFS
    for i in range(n):
        if not visited[i]:
            queue.append(i)
            
            while queue:
                node = queue.pop(0)
                visited[node] = 1
                
                for a in range(n):
                    if computers[node][a] and not visited[a]:
                        queue.append(a)
                
            answer += 1                
        
    return answer

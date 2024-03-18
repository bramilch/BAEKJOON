# Inner Recursive DFS
def solution(n, computers):
    def dfs(node, visited, computers):
        visited[node] = 1
        for neighbor, connected in enumerate(computers[node]):
            if connected and not visited[neighbor]:
                dfs(neighbor, visited, computers)

    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            answer += 1
            
    return answer


# Inner Recursive BFS
# def solution(n, computers):
#     def bfs(node):
#         visited[node] = 1
#         for a in range(n):
#             if computers[node][a] and not visited[a]:
#                 bfs(a)

#     answer = 0
#     visited = [0] * n

#     for i in range(n):
#         if not visited[i]:
#             bfs(i)
#             answer += 1
        
#     return answer
        

# # Queue BFS
# def solution(n, computers):
#     answer = 0
#     queue = []
#     visited = [0] * n
    
#     for i in range(n):
#         if not visited[i]:
#             queue.append(i)
            
#             while queue:
#                 node = queue.pop(0)
#                 visited[node] = 1
                
#                 for a in range(n):
#                     if computers[node][a] and not visited[a]:
#                         queue.append(a)
            
#             answer += 1
    
#     return answer

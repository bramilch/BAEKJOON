def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    queue = []
    
    # 위, 아래, 왼쪽, 오른쪽
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    # 시작 위치
    queue.append((0, 0))
    
    # BFS
    while queue:
        y, x = queue.pop(0)
        
        for i in range(4): # 현재 위치에서 4 방향 다 살펴봄
            ny = y + dy[i] 
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1: # maps 범위 안이고 1일 경우 이동
                    queue.append((ny, nx)) # 갈 수 있는 곳은 다 추가
                    maps[ny][nx] = maps[y][x] + 1 # 이동한 위치에 직접 step 계산. 1로만 표시되어 있기 때문에 가능.
    
    if maps[n - 1][m - 1] == 1: # 목적지가 step 값이 아닌 그대로라면, 갈 수 없다는 의미이므로 -1 return
        return -1
    else:
        answer = maps[n - 1][m - 1] # 목적지에 도달했을 때 step 값
        
    return answer
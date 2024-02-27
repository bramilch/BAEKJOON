def solution(board):
    answer = -1
    
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)] # Down, Up, Left, Right
    
    # 시작 위치, 타겟 위치 찾기
    start_row, start_col = None, None
    target_row, target_col = None, None
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'R':
                start_row, start_col = row, col
            elif board[row][col] == 'G':
                target_row, target_col = row, col

    # BFS
    queue = [(start_row, start_col, 0)] # 시작위치, 거리
    visited = [(start_row, start_col)] # 방문한 위치
    while queue: # queue가 빌 때까지 진행
        current_row, current_col, distance = queue.pop(0)
        
        if (current_row, current_col) == (target_row, target_col):
            answer = distance
            break

        for dr, dc in directions: # 방향 설정
            slipping = 1 # 한 방향으로 계속 이동
            
            while True:
            
                new_row, new_col = current_row + dr * slipping, current_col + dc * slipping
                        
                if new_row < 0 or new_row >= len(board) or new_col < 0 or new_col >= len(board[0]) or board[new_row][new_col] == 'D': # 범위를 벗어나거나 D 만나기 전 위치 찾기
                        if (new_row - dr, new_col - dc) not in visited: # 방문하지 않았다면 visited와 queue에 추가
                                visited.append((new_row - dr, new_col - dc))
                                queue.append((new_row - dr, new_col - dc, distance + 1))
                        break

                slipping += 1
        
    return answer
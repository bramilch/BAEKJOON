def solution(board):
    answer = 0
    board_length = len(board)
    bomb = []
    
    # 8방향
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # 지뢰 위치
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                bomb.append((i, j))
    
    # 지뢰 8방향 1로 바꾸기
    for x, y in bomb:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < board_length and 0 <= ny < board_length:
                board[nx][ny] = 1
    
    # 지뢰, 8방향 제외하고 세기
    for i in board:
        answer += i.count(0)
    
    return answer
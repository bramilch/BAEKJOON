def solution(park, routes):
    answer = []  
    direction = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    
    # 시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start_x, start_y = i, j
                break
    
    for route in routes:
        op, n = route[0], route[2]
        current_x, current_y = start_x, start_y # 이동해 본 위치를 현재 위치로 갱신
        
        # 이동해볼 위치 하나씩 확인하며 start_x, start_y 갱신
        for i in range(int(n)):
            move_x = start_x + direction[op][0]
            move_y = start_y + direction[op][1]

            if 0 <= move_x <= len(park) -1 and 0 <= move_y <= len(park[0]) -1 and (park[move_x][move_y] != 'X'):
                start_x, start_y = move_x, move_y 
            
            else:
                start_x, start_y = current_x, current_y 
                break
    
    # 최종 위치는 current가 아니라 start. 마지막 route는 start로 나옴
    answer = [start_x, start_y]
        
    return answer
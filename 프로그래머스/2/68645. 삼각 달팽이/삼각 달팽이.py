def solution(n):
    answer = []
    
    # 0으로 채워진 정사각형 행 구분 리스트 만들기
    square = [[0] * n for _ in range(n)]
    # 정삼각형 triangle = [[0] * i for i in range(1, n + 1)]
    
    x, y = -1, 0 # 맨 처음 x + 1로 Down해야 하기 때문에 -1
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            
            # Down
            if i % 3 == 0:
                x += 1
                
            # Right
            elif i % 3 == 1:
                y += 1
            
            # Up
            elif i % 3 == 2:
                x -= 1
                y -= 1
                
            square[x][y] = num
            num += 1
    
    # 삼각형에 해당하는 숫자들만 뽑아서 리스트에 append
    for i in range(n):
        for j in range(i + 1):
            answer.append(square[i][j])
            
    return answer
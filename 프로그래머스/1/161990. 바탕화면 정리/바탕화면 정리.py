def solution(wallpaper):
    answer = []
    file_position = []
    length = len(wallpaper)
    width = len(wallpaper[0])
    
    # 파일 위치
    for i, j in enumerate(wallpaper):
        for k in range(len(j)):
            if j[k] == '#':
                file_position += [[i, k]]
    print(file_position)
     
    # [lux 가장 왼쪽, luy 가장 위쪽], [rdx 가장 오른쪽, rdy 가장 아래] 파일 위치 찾기
    lux, luy = min(file_position)[0], min(file_position, key = lambda x: x[1])[1]
    rdx, rdy = max(file_position)[0] + 1, max(file_position, key = lambda x: x[1])[1] + 1
    answer = [lux, luy, rdx, rdy]
    
    return answer
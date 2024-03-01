def solution(board, moves):
    answer = 0
    dic = {}
    nest = []
    
    for i in range(1, len(board) + 1):
        dic[i] = []
        
    for row in board:
        for i, val in enumerate(row, start = 1):
            if val != 0:
                dic[i].append(val)

    for i in moves:
        if bool(dic[i]) == True:
            nest.append(dic[i].pop(0))
        
        while len(nest) > 1 and nest[-1] == nest[-2]:
            nest.pop()
            nest.pop()
            answer += 2
        
        else:
            continue
    
    return answer
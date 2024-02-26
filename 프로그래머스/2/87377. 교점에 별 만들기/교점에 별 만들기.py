def solution(line):
    answer = []
    stars = []
    max_X, min_X, max_Y, min_Y = 0, 0, 0, 0
    
    for i in range(len(line)):
        for j in range(i, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            numer1, numer2, denom = (B*F - E*D), (E*C - A*F), (A*D - B*C)
            if A*D != B*C and numer1 % denom == 0 and numer2 % denom == 0: # x = BF-ED / AD - BC, y = EC - AF / AD - BC
                    x, y = int(numer1 / denom), int(numer2 / denom)
                    stars.append((x, y))

    max_X, min_X = max(stars, key = lambda x: x[0])[0], min(stars, key = lambda x: x[0])[0]
    max_Y, min_Y = max(stars, key = lambda x: x[1])[1], min(stars, key = lambda x: x[1])[1]
    
    answer = [["." for i in range(max_X - min_X + 1)] for j in range(max_Y - min_Y + 1)]

    for x, y in stars:
        answer[max_Y - y][x - min_X] = "*"
    
    answer = ["".join(row) for row in answer]
        
    return answer
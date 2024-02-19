def solution(numbers, hand):
    answer = ''
    left_col = [1, 4, 7]
    right_col = [3, 6, 9]
    center_col = [2, 5, 8, 0]
    left_distance = 0
    right_distance = 0
    left = [3, 0]
    right = [3, 2]
    
    for i in numbers:
        
        # 1) 왼쪽, 오른쪽 확실할 때
        if i in left_col:
            answer += 'L'
            left = [left_col.index(i), 0]
        elif i in right_col:
            answer += 'R'
            right = [right_col.index(i), 2]
        else: # 2) 중앙일 때 왼손, 오른손 위치에서 거리 계산
            i_position = [center_col.index(i), 1]
            left_distance = abs(left[0] - i_position[0]) + abs(left[1] - i_position[1])
            right_distance = abs(right[0] - i_position[0]) + abs(right[1] - i_position[1])
            
            # 2-1) 중앙일 때 왼손, 오른손 거리 같은 경우
            if left_distance == right_distance:
                if hand == 'left':
                    answer += 'L'
                    left = [center_col.index(i), 1]
                else: 
                    answer += 'R'
                    right = [center_col.index(i), 1]
            
            # 2-2) 중앙일 때 왼손, 오른손 거리 다른 경우
            elif left_distance < right_distance:
                answer += 'L'
                left = [center_col.index(i), 1]
            else:
                answer += 'R'
                right = [center_col.index(i), 1]
            
    return answer
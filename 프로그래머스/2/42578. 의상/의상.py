def solution(clothes):
    answer = 1
    hash_map = {}
    
    for clothe, type in clothes:
        if type in hash_map:
            hash_map[type].append(clothe)
        else:
            hash_map[type] = [clothe]
    
    for key in hash_map.keys():
        answer *= len(hash_map[key]) + 1
        
    return answer - 1
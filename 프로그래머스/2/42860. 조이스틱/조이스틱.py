def solution(name):
    
    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    total_moves = sum(alphabet_to_num(ch) for ch in name)

    n = len(name)
    move = n - 1
    
    for idx in range(n):
        next_idx = idx + 1
        
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    total_moves += move
    
    return total_moves


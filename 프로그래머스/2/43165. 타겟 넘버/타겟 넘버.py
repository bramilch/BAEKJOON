def dfs(numbers, target, depth, value):
    global count

    if depth == len(numbers):
        if value == target:
            count += 1        
        return

    dfs(numbers, target, depth + 1, value + numbers[depth])
    dfs(numbers, target, depth + 1, value - numbers[depth])

def solution(numbers, target):
    global count
    count = 0
    
    dfs(numbers, target, 0, 0)
        
    return count
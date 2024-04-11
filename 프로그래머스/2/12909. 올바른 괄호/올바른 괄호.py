def solution(s):
    answer = 0
    stack = []
    
    for left in s:
        if left == '(':
            stack.append(left)
        
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False

    return True
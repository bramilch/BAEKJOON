def solution(n, times):
    answer = 0
    min_time, max_time = 1, max(times)*n
    
    while min_time < max_time:
        mid_time = (min_time + max_time) // 2
        people = 0
        
        for time in times:
            people += mid_time // time
            
        if people >= n:
            max_time = mid_time
            
        else:
            min_time = mid_time + 1
        
    answer = min_time
    
    return answer

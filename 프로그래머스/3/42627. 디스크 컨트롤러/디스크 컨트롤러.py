import heapq

def solution(jobs):
    answer = 0 # 요청에서 종료까지 시간 누적 합
    current = 0 # 현재 시간
    num = 0 # 작업 횟수
    last = -1 # 작업 완료 시간
    heap = []
    
    while num < len(jobs):
        for job in jobs:
            if last < job[0] <= current: # 요청 시간보다 이전 작업 완료 시간보다 커야하고, 현재 시간보다 작거나 같으면
                heapq.heappush(heap, [job[1], job[0]]) # Min Heap에 [소요 시간, 요청 시간]으로 넣어준다.
        
        if heap: # 수행해야 할 작업이 있는 경우
            processing, request = heapq.heappop(heap)
            last = current # 작업 완료 시간에 현재 시간을 넣어준다.
            current += processing # 현재 시간에 소요 시간을 더해준다.
            answer += current - request # 요청에서 종료까지 시간 누적 합
            num += 1 # 시행 횟수
        else:
            current += 1 # heap이 비어있다면 현재 시간이 1 증가
            
    return answer // len(jobs)
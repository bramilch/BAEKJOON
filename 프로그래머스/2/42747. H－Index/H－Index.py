# def solution(citations):
#     citations.sort(reverse = True)
#     left, right = 0, len(citations) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         if citations[mid] <= mid:
#             right = mid - 1
#         else:
#             left = mid + 1
    
#     return left

def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if(citations[i] < i + 1):
            return i

    return len(citations)        



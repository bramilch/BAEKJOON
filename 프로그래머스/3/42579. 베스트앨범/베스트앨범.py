def solution(genres, plays):
    answer = []
    
    # Hash Table
    dict = {}
    total = {}
    for i in range(len(genres)):
        dict[genres[i]] = dict.get(genres[i], []) + [(plays[i], i)]
        total[genres[i]] = total.get(genres[i], 0) + plays[i]
    
    # 장르별 총 재생 횟수 순으로 정렬
    total_sort = sorted(total.items(), key = lambda x: x[1], reverse = True)
    
    # 재생 횟수 많은 장르 순으로 dict의 play 정렬, 맨 앞부터 2곡씩 수록
    for (genre, total) in total_sort:
        dict[genre] = sorted(dict[genre], key = lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in dict[genre][:2]]
    
    return answer
def solution(n, costs):
    
    # 해당 노드가 parent 값인지 확인하고 parent 갱신
    def find(parent, node):
        if parent[node] != node:
            parent[node] = find(parent, parent[node])
        return parent[node]
    
    # 새로운 parent라면 깊이가 더 깊은 rank의 parent 값으로 바꿔서 연결
    def union(parent, rank, node1, node2):
        root1 = find(parent, node1)
        root2 = find(parent, node2)
        
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        
        else:
            parent[root2] = root1
            rank[root1] += 1
    
    answer = 0
    costs.sort(key = lambda x: x[2]) # 건설비용 기준 오름차순 Sort
    parent = [i for i in range(n)] # parent 리스트 초기화
    rank = [0] * n # rank 리스트 초기화
    
    for edge in costs:
        node1, node2, weight = edge
        if find(parent, node1) != find(parent, node2): # 연결되어 있지 않으면 parent를 합치고 비용 추가
            union(parent, rank, node1, node2)
            answer += weight
    
    return answer
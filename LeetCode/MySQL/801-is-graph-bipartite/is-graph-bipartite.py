class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        #DFS
        def traverse(start):
            
            stack = [start]
            colors[start] = True

            while stack:
                node = stack.pop()
                visited.append(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        colors[neighbor] = not colors[node]
                        stack.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
            
            return True

        n = len(graph)
        visited = []
        colors = [False] * n

        for i in range(n):
            if i not in visited:
                if not traverse(i):
                    return False

        return True
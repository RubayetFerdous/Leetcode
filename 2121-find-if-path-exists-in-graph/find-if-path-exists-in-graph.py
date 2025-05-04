class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        graph=[[] for _ in range(n)]
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        visited=[False]*n
        visited[source]=True
        q=[source]
        while q:
            node=q.pop()
            for neighbor in graph[node]:
                if neighbor==destination:
                    return True
                else:
                    if not visited[neighbor]:
                        visited[neighbor]=True
                        q.append(neighbor)
        return False

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph=[[] for _ in range(numCourses)]

        inc=[0]*numCourses
        q=[]
        order=[]

        for i in prerequisites:
            graph[i[1]].append(i[0])
            inc[i[0]]+=1

        for i in range(len(inc)):
            if inc[i]==0:
                q.append(i)
        
        while q:
            node=q.pop(0)
            order.append(node)
            for neighbor in graph[node]:
                inc[neighbor]-=1
                if inc[neighbor]==0:
                    q.append(neighbor)
        if len(order)!=numCourses:
            return []
        return order



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=[[] for i in range(numCourses)]

        inc=[0]*numCourses
        q=[]
        order=[]

        for i in prerequisites:
            graph[i[0]].append(i[1])
            inc[i[1]]+=1

        for i in range(len(inc)):
            if inc[i]==0:
                q.append(i)


        while q:
            node=q.pop()
            order.append(node)
            for neighbor in graph[node]:
                inc[neighbor]-=1
                if inc[neighbor]==0:q.append(neighbor)


        if len(order)!=numCourses:
            return False
            
        return True


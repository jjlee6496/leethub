class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        graph = [[False]*numCourses for _ in range(numCourses)]
        for pre, crs in prerequisites:
            graph[pre][crs] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = True
        
        res = []
        for (u, v) in queries:
            res.append(graph[u][v])
        return res
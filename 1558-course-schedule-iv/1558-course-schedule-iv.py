class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        graph = {i: [] for i in range(numCourses)}
        for pre, crs in prerequisites:
            graph[pre].append(crs)
        
        mem = {}
        def dfs(node):

            if node in mem:
                return mem[node]
            
            cset = set()
            for nei in graph[node]:
                cset.update(dfs(nei))
            cset.add(node)
            mem[node] = cset
            return mem[node]
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for (u, v) in queries:
            res.append(v in mem[u])
        return res
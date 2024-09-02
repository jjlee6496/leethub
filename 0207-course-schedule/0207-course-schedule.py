class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = {i:[] for i in range(numCourses)}
        for n1, n2 in prerequisites:
            adj[n1].append(n2)
        
        path = set()
        visit = set()

        def dfs(node):
            if node in path:
                return True
            if node in visit:
                return False
            
            path.add(node)
            for n2 in adj[node]:
                if dfs(n2):
                    return True
            path.remove(node)
            visit.add(node)
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True
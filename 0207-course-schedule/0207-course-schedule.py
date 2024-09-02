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
        
        visit = [0]*numCourses

        def dfs(node):
            if visit[node] == 1:
                return True
            if visit[node] == 2:
                return False
            
            visit[node] = 1
            for n2 in adj[node]:
                if dfs(n2):
                    return True
            visit[node] = 2

            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True
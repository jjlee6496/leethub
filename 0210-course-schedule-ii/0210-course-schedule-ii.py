class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        order = []
        visit = [0] * numCourses

        def dfs(crs):
            if visit[crs] == 2: # 방문함
                return False
            if visit[crs] == 1: # 방문중
                return True
            
            visit[crs] = 1
            for pre in graph[crs]:
                if dfs(pre):
                    return True
            order.append(crs)
            visit[crs] = 2
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return []
        return order
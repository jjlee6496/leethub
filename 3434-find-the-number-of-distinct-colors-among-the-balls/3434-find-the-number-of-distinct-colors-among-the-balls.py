class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        balls = {}
        colors = {}
        distinct = 0
        res = []

        for ball, new_color in queries:
            if ball in balls:
                old_color = balls[ball]
                colors[old_color] -= 1

                if colors[old_color] == 0:
                    del colors[old_color]
                    distinct -= 1

            balls[ball] = new_color

            if new_color in colors:
                colors[new_color] += 1

            else:
                colors[new_color] = 1
                distinct += 1
            res.append(distinct)
        
        return res
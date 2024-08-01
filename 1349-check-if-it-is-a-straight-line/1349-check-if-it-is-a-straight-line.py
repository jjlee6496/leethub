class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) == 2:
            return True
        (x0, y0) , (x1, y1) = coordinates[:2]
        for x2, y2 in coordinates[2:]:
            if (x2 - x1)*(y0 - y1) != (y2 - y1)*(x0 - x1):
                return False
        return True
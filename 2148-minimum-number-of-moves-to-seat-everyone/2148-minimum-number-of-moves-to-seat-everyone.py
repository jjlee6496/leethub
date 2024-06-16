class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        res = 0
        for i,j in zip(sorted(seats), sorted(students)):
            res += abs(i - j)
        return res
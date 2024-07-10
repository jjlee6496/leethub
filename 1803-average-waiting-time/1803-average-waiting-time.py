class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        t = 0
        total = 0

        for arr, time in customers:
            if t - arr > 0:
                total += t - arr
            else:
                t = arr
            total += time
            t += time
        return total / float(len(customers))
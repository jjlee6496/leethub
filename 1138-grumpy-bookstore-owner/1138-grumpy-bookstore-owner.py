class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        window, max_window = 0, 0
        satisfied = 0
        l = 0
        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]

            else:
                satisfied += customers[r]
            
            if r - l + 1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1
            max_window = max(window, max_window)
        return satisfied + max_window


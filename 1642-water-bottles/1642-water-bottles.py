class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res, remain = numBottles, numBottles
        
        while remain // numExchange:
            div, mod = divmod(remain, numExchange)
            res += div
            remain = (div + mod)
        return res

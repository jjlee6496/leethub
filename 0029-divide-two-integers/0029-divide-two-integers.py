class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = (dividend < 0) ^ (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)
        curr_divisor = divisor
        quotient = 0

        while dividend >= curr_divisor:
            multiple = 1
            while (curr_divisor << 1) <= dividend:
                curr_divisor <<= 1
                multiple <<= 1
            dividend -= curr_divisor
            quotient += multiple

            curr_divisor = divisor
        
        if negative:
            quotient = -quotient
        
        MAX_INT = (1 << 31) - 1
        MIN_INT = -(1 << 31)

        if quotient > MAX_INT:
            return MAX_INT
        elif quotient < MIN_INT:
            return MIN_INT
        else:
            return quotient
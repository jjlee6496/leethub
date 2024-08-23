import re
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        num = 0
        denom = 1

        nums = re.split("/|([+-]?\d+)", expression)
        nums = list(filter(None, nums))
        
        for i in range(0, len(nums), 2):
            c_num = int(nums[i])
            c_denom = int(nums[i+1])

            num = num * c_denom + c_num * denom
            denom = denom * c_denom
        
        div = abs(self.gcd(num, denom))
        num //= div
        denom //= div
        return "{}/{}".format(num, denom)

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
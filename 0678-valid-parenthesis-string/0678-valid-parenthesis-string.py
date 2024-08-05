class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftMin = 0 # all '*' to right
        leftMax = 0 # all '*' to left

        for p in s:
            if p == '(':
                leftMin += 1
                leftMax += 1
            
            elif p == ')':
                # all '*' to left
                leftMin -= 1
                leftMax -= 1

            else:# p == '*':
                leftMin -= 1
                leftMax += 1
            
            if leftMax < 0:
                return False
            
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
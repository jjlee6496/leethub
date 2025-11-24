class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        ans = []
        temp = 0
        for b in nums:
            temp = (temp * 2 + b) % 5
            ans.append(temp == 0)
        return ans
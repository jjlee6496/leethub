class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        temp = ''
        ans = []
        for num in nums:
            temp += str(num)
            if int('0b'+temp, 2) % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        

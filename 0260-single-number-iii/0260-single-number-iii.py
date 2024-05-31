class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        return [num for num, count in dic.items() if count==1]
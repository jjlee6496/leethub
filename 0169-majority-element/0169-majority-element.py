class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = Counter(nums)
        
        return sorted(list(dic.items()), key=lambda x : x[1])[-1][0]
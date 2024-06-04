class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        temp = set()
        for num in nums:
            if -num in cnt:
                temp.add(abs(num))
        return max(temp) if temp else -1
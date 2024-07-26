class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        minV = min(nums)
        maxV = max(nums)

        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        res = []
        for i in range(minV, maxV+1):
            if i not in dic:
                continue
            res.extend([i] * dic[i])
        return res
            
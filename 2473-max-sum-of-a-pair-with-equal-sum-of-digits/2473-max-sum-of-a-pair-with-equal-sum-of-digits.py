class Solution(object):
    def sum2(self, num):
        res = 0
        while num:
            res += num % 10
            num = num // 10
        return res
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(list)
        for i in range(len(nums)):
            num = self.sum2(nums[i])
            heapq.heappush(dic[num], nums[i])
        
        res = -1
        for v in dic.values():
            if len(v) > 1:
                num1, num2 = heapq.nlargest(2, v)
                res = max(res, num1 + num2)
        return res
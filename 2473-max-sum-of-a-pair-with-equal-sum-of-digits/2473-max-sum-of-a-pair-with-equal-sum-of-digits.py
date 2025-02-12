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
        dic = defaultdict(int)
        res = -1
        for num in nums:
            s = self.sum2(num)
            
            if s in dic:
                if dic[s] + num > res:
                    res = dic[s] + num
                if dic[s] < num:
                    dic[s] = num
            else:
                dic[s] = num
        return res
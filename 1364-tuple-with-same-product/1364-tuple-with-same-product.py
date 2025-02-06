class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prods = {}
        res = 0
        for i in range(len(nums)):
            n1 = nums[i]
            for j in range(i+1, len(nums)):
                n2 = nums[j]
                prods[n1*n2] = prods.get(n1*n2, 0) + 1
        for v in prods.values():
            if v > 1:
                res += (v * (v-1) // 2) * 8
        return res
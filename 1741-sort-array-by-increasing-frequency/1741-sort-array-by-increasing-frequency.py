class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = Counter(nums)
        res = []
        temp = [[k]*v for k,v in sorted(cnt.items(), key = lambda (x, y): (y, -x))]
        for x in temp:
            res.extend(x)
        return res
        
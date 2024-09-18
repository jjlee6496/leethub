class Solution(object):

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a, b):
            if a + b < b + a:
                return 1
            if a + b > b + a:
                return -1
            else:
                return 0

        nums = map(str, nums)
        nums.sort(cmp=compare)
        res = ''.join(nums)
        return '0' if res[0] == '0' else res
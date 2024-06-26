class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, m = 0, 0
        odds = 0
        res = 0
        for right in range(len(nums)):
            if nums[right]%2:
                odds += 1

            while odds > k:
                if nums[left] % 2:
                    odds -= 1
                left += 1
                m = left


            if odds == k:
                while not nums[m]%2:
                    m += 1
                res += m - left + 1

        return res

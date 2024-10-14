class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        score = 0
        nums = [-x for x in nums]
        heapq.heapify(nums)
        while k:
            num = -heapq.heappop(nums)
            print(num)
            score += num
            heapq.heappush(nums, -int(math.ceil(num/3.0)))
            k -= 1
        return score
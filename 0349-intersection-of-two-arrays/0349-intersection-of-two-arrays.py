class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        l = r = 0
        n, m = len(nums1), len(nums2)
        ans = set()
        while l < n and r < m:
            if nums1[l] == nums2[r]:
                ans.add(nums1[l])
                l += 1
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        return list(ans)
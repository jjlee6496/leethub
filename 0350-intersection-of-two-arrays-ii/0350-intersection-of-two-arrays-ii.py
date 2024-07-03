class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        i, j = 0, 0
        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()
        res = []
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return res
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        ids = {}
        for i, val in nums1:
            ids[i] = ids.get(i, 0) + val
        
        for i, val in nums2:
            ids[i] = ids.get(i, 0) + val
        
        return sorted([(i, v) for i, v in ids.items()])
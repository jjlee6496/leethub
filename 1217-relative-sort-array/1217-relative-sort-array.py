class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        cnt = Counter(arr1)
        res = []
        for num in arr2:
            res.extend([num]*cnt[num])
            del cnt[num]
        for k, v in sorted(cnt.items(), key=lambda x: x[0]):
            res.extend([k]*v)
        return res
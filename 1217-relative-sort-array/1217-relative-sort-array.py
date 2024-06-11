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
            for _ in range(cnt[num]):
                res.append(num)
            del cnt[num]
        for k, v in sorted(cnt.items(), key=lambda x: x[0]):
            for _ in range(v):
                res.append(k)
        return res
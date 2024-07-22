class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        dic = defaultdict(int)
        for i, n in enumerate(names):
            dic[heights[i]] = n
        ans = []
        for k in sorted(dic.keys(), reverse=True):
            ans.append(dic[k])
        return ans

        
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            return [strs]
        ans = []
        dic = defaultdict(list)
        for i in range(len(strs)):
            dic[''.join(sorted(strs[i]))].append(strs[i])
        
        return [x for x in dic.values()]
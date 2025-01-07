class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        temp = ' '.join(words)
        return [w for w in words if temp.count(w) > 1]
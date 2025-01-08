class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                res += self.is_true(words[i], words[j])
        return res

    def is_true(self, word1, word2):
        n, m = len(word1), len(word2)
        if n > m:
            return 0
        if word2.startswith(word1) and word2.endswith(word1):
            return 1
        
        return 0
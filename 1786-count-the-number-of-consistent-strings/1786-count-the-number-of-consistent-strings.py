class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        bit_mask = 0
        for a in allowed:
            bit = 1 << (ord(a) - ord('a'))
            bit_mask |= bit
        
        res = len(words)
        for word in words:
            for w in word:
                if not bit_mask & (1 << ord(w) - ord('a')):
                    res -= 1
                    break
        return res
            

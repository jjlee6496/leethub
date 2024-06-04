class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        def is_pal(word):
            for i in range(len(word)//2):
                if word[i] != word[~i]:
                    return False
            return True
        
        for word in words:
            if is_pal(word):
                return word
        return ''
        
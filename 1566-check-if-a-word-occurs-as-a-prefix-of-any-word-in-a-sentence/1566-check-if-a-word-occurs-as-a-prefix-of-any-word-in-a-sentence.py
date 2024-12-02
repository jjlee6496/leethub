class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i].startswith(searchWord):
                return i + 1
        return -1
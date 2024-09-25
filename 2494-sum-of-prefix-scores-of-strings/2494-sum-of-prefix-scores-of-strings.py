class TrieNode:
    def __init__(self):
        self.children = {}
        self.cnt = 0


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.cnt += 1


    def search(self, word):
        curr = self.root
        score = 0
        for c in word:
            if c not in curr.children:
                break
            curr = curr.children[c]
            score += curr.cnt
        return score

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        dic = PrefixTree()

        for word in words:
            dic.insert(word)
        
        return [dic.search(word) for word in words]
class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(words)
        pre = [0] * (n + 1)
        vowels = set('aeiou')
        for i in range(n):
            pre[i + 1] = pre[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                pre[i + 1] += 1
        return [pre[end + 1] - pre[start] for start, end in queries]
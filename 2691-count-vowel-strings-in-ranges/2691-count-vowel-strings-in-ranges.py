class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        mem = []
        s = 0 # prefix sum
        vowels = set('aeiou')
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                s += 1
            mem.append(s)
        print(mem)
        res = []
        for start, end in queries:
            if start == 0:
                res.append(mem[end])
            else:
                res.append(mem[end] - mem[start-1])
        return res
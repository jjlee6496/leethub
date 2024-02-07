class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
        ans = ''
        for c, f in sorted([(k, v) for k, v in dic.items()], key=lambda x: -x[1]):
            ans += c*f
        return ans
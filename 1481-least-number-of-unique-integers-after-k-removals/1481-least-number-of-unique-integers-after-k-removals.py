class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = Counter(arr)
        dic2 = sorted(dic, key=lambda x: dic[x])

        for num in dic2:
            if k >= dic[num]:
                k -= dic[num]
                del dic[num]
            else:
                break
        return len(dic)
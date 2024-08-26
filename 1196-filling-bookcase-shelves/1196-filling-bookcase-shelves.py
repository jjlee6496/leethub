class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        mem = {}
        def dfs(i, remain, height):
            if i == len(books):
                return height
            if (i, remain, height) in mem:
                return mem[(i, remain, height)]
            # 다음 칸에 넣기
            res1 = height + dfs(i+1, shelfWidth - books[i][0], books[i][1])
            res2 = float('inf')
            if remain >= books[i][0]:
                # 같은 칸에 넣기
                res2 = dfs(i+1, remain - books[i][0], max(height, books[i][1]))
            mem[(i, remain, height)] = min(res1, res2)
            return mem[(i, remain, height)]
        return dfs(0, shelfWidth, 0)

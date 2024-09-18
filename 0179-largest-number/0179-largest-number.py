class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class compare(str):
            def __lt__(a, b):
                return a+b > b+a
        nums = list(map(str, nums))
        nums.sort(key=compare)
        res = ''.join(nums)
        return '0' if res[0]=='0' else res
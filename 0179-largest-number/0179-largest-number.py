class compare(str):
    def __lt__(a, b):
        return a+b > b+a
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=compare)
        res = ''.join(nums)
        return '0' if res[0]=='0' else res
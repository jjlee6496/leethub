import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            return int(a+b) - int(b+a) 

        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        res = ''.join(nums)
        return '0' if res[0]=='0' else res
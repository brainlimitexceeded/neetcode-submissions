class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        d = dict()
        for n in sorted(nums):
            if n-1 in d:
                d.update({n:(1+d[n-1])})
            else:
                d.update({n:1})
        return max([v for v in d.values()])
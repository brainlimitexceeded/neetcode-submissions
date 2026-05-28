class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return True if len(nums) != len(s) else False
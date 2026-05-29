class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [1 for i in range(len(nums))]
        ans = []
        for i in range(len(nums)):
            left.append(nums[i] if len(left) == 0 else nums[i]*left[i-1])
        for j in range(len(nums)-1,0,-1):
            right[j] = (nums[j] if j == (len(nums)-1) else nums[j]*right[j+1])
        for k in range(len(nums)):
            ans.append((left[k-1] if k>0 else 1)*(right[k+1] if k<len(nums)-1 else 1))
        return ans
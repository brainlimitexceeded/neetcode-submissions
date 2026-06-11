class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)
        ans = 0
        for i in range(len(height)):
            left[i] = max(height[i], 0 if i == 0 else left[i-1])
            j = len(height)-i-1
            right[j] = max(height[j], 0 if i==0 else right[j+1])
        for i in range(1,len(height)-1):
            boundary = min(left[i],right[i])
            if boundary > height[i]:
                ans+=(boundary-height[i])
        return ans
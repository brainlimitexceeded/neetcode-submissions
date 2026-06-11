class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        right = [0]*len(heights)
        for i in range(len(heights)-1,-1):
            right[i] = max(heights[i], 0 if i == len(heights)-1 else right[i+1])
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                ans = max(ans, (min(heights[i],heights[j])*(j-i)))
        return ans
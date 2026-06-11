class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left = [1000]*len(prices)
        right = [0]*len(prices)
        for i in range(len(prices)):
            j = len(prices)-i-1
            left[i] = min(prices[i], 1000 if i==0 else left[i-1])
            right[j] = max(prices[j], 0 if i==0 else right[j+1])
        for i in range(len(prices)):
            ans = max(right[i]-left[i], ans)
        return ans
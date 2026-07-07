class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # 2,1,

        # ans is 2

        # 2,1,0

        # ans is 2

        # 4

        # ans is 4
        dq = deque()
        for i in range(len(nums)):
            while len(dq)>0 and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)
            while i-dq[0]>=k:
                dq.popleft()
            # print(i,stack)
            if i>=k-1:
                ans.append(nums[dq[0]])
        return ans
class Solution:
    # # i = j+hm
    # i+j+hm = 0
    # hm = -i-j
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        # print(nums)
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                hm = set()
                pairs = set()
                for j in range(i+1,len(nums)):
                    if -(nums[i]+nums[j]) in hm:
                        if (-nums[i]-nums[j],nums[j]) not in pairs and (nums[j], -nums[i]-nums[j]) not in pairs:
                            # print(hm,pairs)
                            pairs.add((-nums[i]-nums[j],nums[j]))
                    hm.add(nums[j])
                for p in pairs:
                    ans.append([nums[i],p[0],p[1]])
        return ans
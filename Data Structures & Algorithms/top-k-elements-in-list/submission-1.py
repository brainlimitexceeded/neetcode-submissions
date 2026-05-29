class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = dict()
        d = dict()
        for n in nums:
            if n in d:
                prev = d[n]
                d[n]+=1
                bucket[prev].remove(n)
            else:
                d.update({n:1})
            if d[n] not in bucket:
                bucket[d[n]] = set()
            bucket[d[n]].add(n)
        ans = []
        # print(bucket)
        for i in range(len(nums),0,-1):
            if i in bucket:
                while k>0 and len(bucket[i])>0:
                    ans.append(bucket[i].pop())
                    k-=1
            if k<=0:
                break
        return ans

        
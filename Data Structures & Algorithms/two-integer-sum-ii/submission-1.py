class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bs (i,j,target):
            # print(i,j,target)
            if i>=j:
                return j
            mid = (i+j)//2
            # print(mid)
            if numbers[mid] < target:
                return bs(mid+1,j,target)
            else:
                return bs(i,mid,target)

        for i in range(len(numbers)):
            index = bs(i+1,len(numbers)-1,target-numbers[i])
            # print(i,index)
            if numbers[index]+numbers[i] == target:
                return [i+1,index+1]
        
            
            
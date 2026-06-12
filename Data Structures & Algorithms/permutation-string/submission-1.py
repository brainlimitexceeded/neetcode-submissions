class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = [0]*26
        for s in s1:
            arr[ord(s)-ord('a')]+=1
        brr = [0]*26
        i = 0
        j = 0
        while j<len(s2):
            if j-i+1>len(s1):
                brr[ord(s2[i])-ord('a')]-=1
                i+=1
            print(i,j,arr,brr)
            brr[ord(s2[j])-ord('a')]+=1
            j+=1
            if arr == brr:
                return True
        return False

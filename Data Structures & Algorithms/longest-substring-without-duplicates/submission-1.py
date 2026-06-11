class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [0]*10000
        i = 0
        j = 0
        ans = 0
        while j<len(s):
            # print(i,j,arr)
            while arr[ord(s[j])-ord('a')]>=1:
                arr[ord(s[i])-ord('a')]-=1
                i+=1
            arr[ord(s[j])-ord('a')]+=1
            ans = max(ans, j-i+1)
            j+=1
        return ans


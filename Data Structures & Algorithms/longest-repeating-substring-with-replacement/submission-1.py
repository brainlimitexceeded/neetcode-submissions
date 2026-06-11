class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0]*26
        i = 0
        j = 0
        ans = 0
        def holds():
            maxi = max(arr)
            tot = sum(arr)
            output = tot-maxi<=k
            print(arr,output)
            return output
        while j<len(s):
            arr[ord(s[j])-ord('A')]+=1
            print(i,j,arr)
            while not holds():
                arr[ord(s[i])-ord('A')]-=1
                i+=1
            print(i,j,j-i+1)
            ans = max(ans,j-i+1)
            j+=1
        return ans
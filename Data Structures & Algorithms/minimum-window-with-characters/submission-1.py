class Solution:
    def minWindow(self, s: str, t: str) -> str:
        arr = [0]*200
        brr = [0]*200
        ans = ""
        for tt in t:
            arr[ord(tt)-ord('a')]+=1
        for i in range(len(s)):
            brr = [0]*200
            # print(arr,brr,i)
            for j in range(i,len(s)):
                brr[ord(s[j])-ord('a')]+=1
                if (j-i+1 <= len(ans)) or ans == "":
                    for k in range(200):
                        # print("here",i,j)
                        if arr[k]>brr[k]:
                            # print(i,j)
                            k-=1
                            break
                    if k == 199:
                        ans = s[i:j+1]
        return ans

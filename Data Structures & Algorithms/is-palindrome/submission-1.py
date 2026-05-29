class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1
            # print(i,j,len(s))
            if i>=j:
                return True
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
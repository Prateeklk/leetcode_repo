class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        res = s[0]
        count = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1] and (j - i + 1) > count:
                    res = s[i:j+1]
                    count = j - i + 1
        return res

                    

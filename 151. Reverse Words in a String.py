class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 0:
            return ""
        res = ""
        split_str = s.split()
        for i in range(len(split_str)):
            res +=' '+split_str[len(split_str) - (i+1)]
        return res.strip()

        
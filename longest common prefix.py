class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for s in zip(*strs):
            if len(set(s)) == 1:
                res+=s[0]
            else:
                return res
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(haystack.find(needle)!=-1):
            return haystack.find(needle)
        return -1
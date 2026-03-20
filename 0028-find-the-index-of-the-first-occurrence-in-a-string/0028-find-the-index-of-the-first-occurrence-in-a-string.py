class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        while i<=(len(haystack)-len(needle)):
            j=0
            while(j!=len(needle)):
                if needle[j]==haystack[i+j]:
                    j+=1
                else:
                    break
            if j==len(needle):
                return i
            else:
                i+=1
        return -1
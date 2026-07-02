class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = ""
        longest = ""
        i = 0
        while i < len(s):
            if s[i] not in s1:
                s1 += s[i]
                if len(s1) > len(longest):
                    longest = s1
                i += 1
            else:
                while s[i] in s1:
                    s1 = s1[1:]

        return len(longest)
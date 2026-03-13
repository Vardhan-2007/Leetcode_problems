class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        s=s.split(' ')
        return len(s[len(s)-1])
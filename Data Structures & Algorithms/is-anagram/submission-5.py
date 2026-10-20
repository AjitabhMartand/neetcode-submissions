class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = 1+freq.get(s[i],0)
        freq1={}
        for i in range(len(t)):
            freq1[t[i]] = 1 +freq1.get(t[i],0)
        return freq==freq1
        
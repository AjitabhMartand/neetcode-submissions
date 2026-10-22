class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countT={}
        res = 0
        left = 0
        maxf = 0
        for i in range(len(s)):
            countT[s[i]] = 1 + countT.get(s[i],0)
            maxf = max(maxf,countT[s[i]])
            while (i-left+1)-maxf>k:
                countT[s[left]] -=1
                left += 1
            res = max(res,i-left+1)
        return res
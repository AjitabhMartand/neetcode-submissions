class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countT={}
        res=0
        maxl=0
        l=0
        for i in range(len(s)):
            countT[s[i]] = 1+countT.get(s[i],0)
            maxl = max(maxl,countT[s[i]])
            while  (i-l+1)-maxl>k:
                countT[s[l]] -=1
                l+=1
            res = max(res,i-l+1)
        return res

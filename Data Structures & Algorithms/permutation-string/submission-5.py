class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = {}
        for c in s1:
            c1[c] = 1 + c1.get(c,0)
        count2 = {}
        l = 0
        for i in range(len(s2)):
            count2[s2[i]] = 1 + count2.get(s2[i],0)
            if i-l+1>len(s1):
                count2[s2[l]] -= 1
                if count2[s2[l]]==0:
                    del count2[s2[l]]
                l+= 1
            if c1==count2:
                return True
        return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1={}
        for s in s1:
            c1[s] = 1+c1.get(s,0)
        c2 = {}
        l=0
        for i in range(len(s2)):
            c2[s2[i]] = 1+c2.get(s2[i],0)
            if i-l+1>len(s1):
                c2[s2[l]] -=1
                if c2[s2[l]]==0:
                    del c2[s2[l]]
                l+=1
            if c1 == c2:
                return True
        return False
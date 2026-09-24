class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ans = {}
        for i in s:
            ans[i] = 1+ans.get(i,0)
        ans1 = {}
        for i in t:
            ans1[i] = 1+ans1.get(i,0)
        return ans==ans1

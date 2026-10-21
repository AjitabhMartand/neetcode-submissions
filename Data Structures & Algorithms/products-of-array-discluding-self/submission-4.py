class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        p = 1
        for i in range(len(nums)):
            ans.append(p)#1128
            p*=nums[i]
        s=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=s#8122448
            s*=nums[i]
        return ans
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        having={}
        for i,num in enumerate(nums):
            diff = target-num
            if diff in having:
                return [having[diff],i]
            having[num]=i
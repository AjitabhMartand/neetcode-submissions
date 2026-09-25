class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i,num in enumerate(numbers):
            diff = target - num
            if diff in mp:
                return [mp[diff],i+1]
            mp[num]=i+1
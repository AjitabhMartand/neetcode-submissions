class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest=0
        for num in nums:
            if num - 1 not in store:
                l=1
                while num+l in store:
                    l+=1
                longest = max(longest,l)
        return longest
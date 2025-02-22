class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [hashmap[difference],i]
            hashmap[num] = i
        return []
        
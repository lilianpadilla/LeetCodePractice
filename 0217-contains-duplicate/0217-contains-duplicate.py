class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        if nums is None:
            return False
        
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = num
        return False
        
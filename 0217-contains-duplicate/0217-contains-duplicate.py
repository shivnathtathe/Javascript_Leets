class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<0:
            return False
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
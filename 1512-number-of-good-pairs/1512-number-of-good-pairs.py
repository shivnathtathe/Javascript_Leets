class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        if not nums:
            return 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] == nums[j]) and i > j:
                    count +=1
        return count
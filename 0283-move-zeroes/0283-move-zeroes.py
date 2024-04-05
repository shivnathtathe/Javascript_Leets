class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.remove(0)
            else:
                i += 1
        nums += [0] * count

        
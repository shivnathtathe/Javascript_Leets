class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        str_=''
        for num in nums:
            str_ +=str(num)
            
        return [int(x) for x in str_]
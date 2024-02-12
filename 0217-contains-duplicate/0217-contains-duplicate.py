import collections as  cln
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<0:
            return False
        result = cln.Counter(nums)
        counter_stack = []
        for i,j in result.items():
            counter_stack.append(j)
        
        for count in counter_stack:
            if count >=2:
                return True
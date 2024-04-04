class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        count = 0
        for char in s:
            if char == '(':
                count +=1
            elif char == ')':
                count -=1
            else:
                continue
            max_count = max(max_count,count)
        return max_count
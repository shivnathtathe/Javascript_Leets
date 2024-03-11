class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str_ =""
        
        for num in range(len(s)):
            for j in indices:
                if num == j:
                    str_ += s[indices.index(j)]
        return str_
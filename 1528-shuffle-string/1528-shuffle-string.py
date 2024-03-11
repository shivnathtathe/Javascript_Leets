from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create a dictionary to map indices to characters
        char_map = {}
        for index, char in zip(indices, s):
            char_map[index] = char
        
        # Reconstruct the string using the dictionary
        result = ""
        for i in range(len(indices)):
            result += char_map[i]
        
        return result

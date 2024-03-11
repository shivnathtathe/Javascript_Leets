class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        new_list = s.split(" ")
        str_ = ""
        new_list2 = []
        for x in range(k):
            new_list2.append(new_list[x])
        return " ".join(new_list2)
            
            
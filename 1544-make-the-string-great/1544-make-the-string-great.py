class Solution:
    def makeGood(self, s: str) -> str:
        def helper(string):
            i = 0
            while i < len(string) - 1:
                if (string[i].lower() == string[i+1].lower()) and (string[i] != string[i+1]):
                    string = string[:i] + string[i+2:]
                    i = max(0, i - 1)
                else:
                    i += 1
            return string
        return helper(s)

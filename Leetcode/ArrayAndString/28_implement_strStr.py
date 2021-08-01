class Solution:
    def strStr(self, string: str, substring: str) -> int:
        if not substring:
            return 0
        if len(string) < len(substring):
            return -1
        if string == substring:
            return 0
        # Find possible match char from string, then do the whole searching for the string
        
        for i in range(len(string) - len(substring) + 1):
            if string[i] != substring[0]:
                continue
            if string[i:i + len(substring)] == substring:
                return i
        return -1
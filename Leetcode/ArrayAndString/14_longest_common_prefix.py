class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        n_max = float('inf')
        minStr = 0
        n = 0
        for item in strs:
            if len(item) < n_max:
                n_max = len(item)
                minStr = item
            n_max = min(n_max, len(item))
            
        i = 0
        # print (n_max)
        while n < n_max:
            curChar = strs[0][n]
            strIdx = 1
            while strIdx != len(strs):
                if curChar != strs[strIdx][n]:
                    return strs[0][0:n]
                strIdx += 1
            # print (n, " is done")
            n += 1
            
        return minStr

## Better

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = '' if not strs else strs.pop()
        for i, c in enumerate(first)
            for s in strs:
                if i >= len(s) or c != s[i]:
                    return first[:i]

        return first



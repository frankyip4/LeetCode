class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        m = len of the first string in the list
        n = len of the list
        Run time: O(mn)
        """
        common = ""
        index = 0
        if len(strs) == 0:
            return common
        elif len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            char = strs[0][i]
            for item in strs[1:]:
                if len(item) <= i or item[i] != char:
                    return common
            common += char
        return common

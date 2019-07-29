class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        n = len of the list
        runtime: O((min length of all string) * n)
        """
        common = ""
        if not strs:
            return common
        shortest_str = min(strs, key=len)
        for i in range(len(shortest_str)):
            char = shortest_str[i]
            for item in strs:
                if item[i] != char:
                    return common
            common += char
        return common


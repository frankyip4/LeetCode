class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Runtime: O(n^2)
        Explanation: Find the length of string without finding repeating characters for s[i:]
        for every i
        ie func("abcabcbb") -> max(3, func("bcabcbb")) and so on
        """
        maxNum = 0
        for i in range(len(s)):
            search = set()
            result = 0
            count = 0
            for char in s[i:]:
                if char in search:
                    result = max(count, result)
                    search = set()
                    count = 0
                search.add(char)
                count += 1
            maxNum =  max(max(result, count), maxNum)
        return maxNum

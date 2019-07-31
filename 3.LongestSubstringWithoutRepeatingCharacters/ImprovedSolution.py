class Solution:
    """
    Runtime: O(n)
    worst case runtime O(2n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxNum = 0
        i = j = 0
        se = set()
        while j <= len(s) - 1:
            if (s[j] in se):
                se.remove(s[i])
                i += 1
            else:
                se.add(s[j])
                j += 1
                maxNum = max(j - i, maxNum)
        return maxNum

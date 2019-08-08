class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Bad runtime
        :param s:
        :type s:
        :return:
        :rtype:
        """

        maxS = ""

        for i in range(len(s)):
            currS = s[i]
            j = i - 1
            k = i + 1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    currS = s[j] + currS + s[k]
                    j -= 1
                    k += 1
                else:
                    break
            if len(maxS) < len(currS):
                maxS = currS
            if i >= len(s) - 1:
                break
            if s[i] == s[i + 1]:
                j = i - 1
                k = i + 2
                currS = s[i] + s[i + 1]
                while j >= 0 and k < len(s):
                    if s[j] == s[k]:
                        currS = s[j] + currS + s[k]
                        j -= 1
                        k += 1
                    else:
                        break
                if len(maxS) < len(currS):
                    maxS = currS
        return maxS

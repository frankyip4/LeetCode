class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Runtime O(Kn)
        but minor detail can be improve
        decrease constant K
        :param s:
        :type s:
        :param numRows:
        :type numRows:
        :return:
        :rtype:
        """
        if numRows == 1:
            return s
        result = ""
        i = 0
        while i * (2 * numRows - 2) < len(s):
            result += s[i * (2 * numRows - 2)]
            i += 1

        for k in range(1, numRows - 1):
            flip = True
            i = 0
            ind = k
            while ind < len(s):
                result += s[ind]
                if flip:
                    ind += (2 * (numRows - k) - 2)
                else:
                    ind += 2 * k
                flip = not (flip)
        i = 0
        while (numRows - 1) + i * (2 * numRows - 2) < len(s):
            result += s[(numRows - 1) + i * (2 * numRows - 2)]
            i += 1
        return result

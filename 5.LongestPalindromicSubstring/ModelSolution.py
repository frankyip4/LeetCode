# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

class Solution:
    def __init__(self):
        self.longestLength = 0
        self.longestString = ""
    def longestPalindrome(self, s: str) -> str:
        # 0.1 A string of length 0 has a Palindromic substring of length 0.
        # 0.2 A string of length 1 has a Palindromic substring of length 1.
        # 0.3 Else initialize the longest length to 1.
        if len(s) == 0 or len(s) == 1:
            return s
        else:
            self.longestLength = 1
            self.longestString = s[0]
        # 1. Begin at the center of the string and form the largest palindrome that can be found.  There are two cases:
        #    A. Even-length palindrome - these are formed by selecting two string indices as the starting point for center of the palindrome
        #    B. Odd-length palindrome - these are formed by selecting one string index as the starting point for center of the palindrome
        middle = int(len(s)/2)
        # Odd: check middle and left of middle
        left = middle - 1
        right = middle + 1
        while (2*(left+1)+1) > self.longestLength: # only need to check until quantity is smaller than the longest palindrome discovered to date (can't find a smaller one in substring less than the length.)
            self.checkPalindrome(s, left,right)
            left -= 1
            right -= 1
        # Odd: check all right of middle
        # middle +1 is center to start.
        left = middle
        right = middle + 2
        while (2*(len(s)-right)+1) > self.longestLength: # only need to check until twice the remaining right substring is smaller than the longest palindrome discovered to date (can't find a smaller one in substring less than the length.)
            self.checkPalindrome(s, left,right)
            left += 1
            right += 1
        # Even: check left of middle
        left = middle - 1
        right = middle
        while (2*(left+1)) > self.longestLength: # only need to check until 2*left is smaller than the longest palindrome discovered to date (can't find a smaller one in substring less than the length.)
            self.checkPalindrome(s, left,right)
            left -= 1
            right -= 1
        # Even: check right of middle
        left = middle
        right = middle + 1
        while (2*(len(s)-right)) > self.longestLength: # only need to check until twice the remaining right substring is smaller than the longest palindrome discovered to date (can't find a smaller one in substring less than the length.)
            self.checkPalindrome(s,left,right)
            left += 1
            right += 1
        return self.longestString

    def checkPalindrome(self, s, left, right):
        palindrome = True
        while palindrome:
            if (left < 0) or (right >= len(s)):
                # out of range
                palindrome = False
            elif s[left] == s[right]:
                if right+1-left > self.longestLength:
                    self.longestLength = right+1-left
                    self.longestString = s[left:right+1]
                # attempt to extend palindrome:
                left -= 1
                right += 1
            else:
                # end of palindrome, we've already recorded the longest
                palindrome = False

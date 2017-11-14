# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Example:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example:
# Input: "cbbd"
# Output: "bb"
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        start = 0
        n = len(s)

        for i in xrange(n):
        	if i - maxlen >= 1 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
        		start = i - maxlen - 1
        		maxlen += 2
        		continue
        	if i - maxlen >= 0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
        	 	start = i - maxlen
        	 	maxlen += 1
        return s[start:start + maxlen]
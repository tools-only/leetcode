# 10. Regular Expression Matching
# Implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """ 
        if len(p) == 0:
        	return len(s) == 0
        if len(p) == 1:
        	if (len(s) == 1) and (p == s or p == '.'):
        		return True
        	else:
        		return False
        if p[1] != '*':
        	if (len(s) > 0) and (p[0] == s[0] or p[0] == '.'):
        		return self.isMatch(s[1:], p[1:])
        	return False
        else:
        	while (len(s) > 0) and (p[0] == '.' or p[0] == s[0]):
        		if self.isMatch(s, p[2:]):
        			return True
        		s = s[1:]
        	return self.isMatch(s, p[2:])		

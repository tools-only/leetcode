class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        num = 0
        for i in range(0, l - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]
        return num + roman[s[l - 1]]
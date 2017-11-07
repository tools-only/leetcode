# 6. ZigZag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = []
        interval = 2 * numRows - 2
        
        for i in range(0,numRows):
            temp1 = i
            temp2 = interval - i
            if temp1 == 0 or temp1 == numRows - 1:
                while temp1 < len(s):
                    res.append(s[temp1])
                    temp1 = temp1 + interval
            else:
                while temp1 < len(s):
                    res.append(s[temp1])
                    temp1 = temp1 + interval
                    if temp2 < len(s):
                        res.append(s[temp2])
                        temp2 = temp2 + interval
                        
        result = ''.join(res)
        return res
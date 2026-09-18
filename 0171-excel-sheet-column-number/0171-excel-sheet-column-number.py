class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        s=0
        for ct in columnTitle:
                s = s * 26 + (ord(ct) - ord('A') + 1)
        
        return s
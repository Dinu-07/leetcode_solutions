class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(1,len(s)+1):
            order = (abs(ord(s[i-1]) - ord('z')) + 1 ) * i
            result = result + order
        return result
        
class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)-1):
            j = i+1
            if s[i] != s[j]:
                if s.count(s[i]) == int(s[i]) and s.count(s[j]) == int(s[j]):
                    return s[i] + s[j]
        return ""

        
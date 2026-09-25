class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = s.split()
        i = len(s1) -1
        l = len(s1[i])
        return l
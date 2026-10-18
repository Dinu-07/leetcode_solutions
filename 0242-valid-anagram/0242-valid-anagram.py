class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for i in t:
         if i in s and s.count(i)==t.count(i):
            pass
         else:
            return False
        else:
         return True
        
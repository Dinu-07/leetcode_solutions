class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        set1 = set(s)
        set2 = set(t)
        for i in set2:
            if i in set1 and s.count(i) == t.count(i):
                pass
            else:
                return False
        else:
            return True
        
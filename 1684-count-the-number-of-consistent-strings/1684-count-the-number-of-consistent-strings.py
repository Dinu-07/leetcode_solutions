class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words :
            for j in i:
                if j in allowed:
                    pass
                else:
                    break
            else:
                count += 1
        return count

                

        
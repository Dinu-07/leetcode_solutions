class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        list_ = set(words2)
        result  = 0
        for i in words1 :
            if words1.count(i) == 1:
                if i in list_ and words2.count(i)==1:
                    result+=1
        return result